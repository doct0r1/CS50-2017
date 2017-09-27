from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp

from helpers import *

# configure application
app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# custom filter
app.jinja_env.filters["usd"] = usd

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/")
@login_required
def index():
    # Select each symbol owned by the user and it's amount
    portfolioSymbols = db.execute("SELECT shares, symbol FROM portfolio WHERE id = :id", id=session["user_id"])

    # temporary variable for total worth (cash + share)
    totalCash = 0

    # Update each symbol price & total
    for portfolioSymbol in portfolioSymbols:
        symbol = portfolioSymbol["symbol"]
        shares = portfolioSymbol["shares"]
        stock = lookup(symbol)
        total = shares * stock["price"]
        totalCash += total
        db.execute("UPDATE portfolio SET proce=:price, total=:total WHERE id=:id AND symbol=:symbol", price=usd(stock["price"]), total=usd(total), id=session["user_id"], symbol=symbol)

    # Update user's cash in portfolio
    updateCash = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])

    # Update the total (cash + shares)
    totalCash += updateCash[0]["cash"]

    # Print portfolio in index homepage
    updatePortfolio = db.execute("SELECT * from portfolio WHERE id=:id", id=session["user_id"])

    return render_template("index.html", stocks=updatePortfolio, cash=usd(updateCash[0]["cash"]), total=usd(totalCash))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock."""

    # if the user is get from link after login or register!
    if request.method == "GET":
        return render_template("buy.html")

    # else from post means there's an input (symbol & shares)
    else:
        # ensure proper symbol
        stock = lookup(request.form.get("symbol"))
        if not stock:
            return apology("Invalid Symbol")
        
        # ensure proper number of shares
        try:
            shares = int(request.form.get("shares"))
            if shares < 0:
                return apology("Shares must be positive integer")
        except:
            return apology("Shares must be positive integer.")

        # select user's cash by returning to his ID
        money = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])

        # check if he has enough money
        if not money or float(money[0]["cash"]) < stock["price"] * shares:
            return apology("Not Enough Money")

        # Update history
        db.execute("INSERT INTO history (symbol, shares, price, id) VALUES(:symbol, :shares, :price, :id)", symbol=stock["symbol"], shares=shares, price=usd(stock["price"]), id=session["user_id"])

        # Update user cash
        db.execute("UPDATE users SET cash = cash - :purchase WHERE id=:id", id=session["user_id"], purchase=stock["price"] * float(shares))

        # Select user shares from that symbol
        userShares = db.execute("SELECT shares FROM portfolio WHERE id=:id AND symbol=:symbol", id=session["user_id"], symbol=stock["symbol"])

        # If there's no shares of that symbol, create new stock object
        if not userShares:
            db.execute("INSERT INTO portfolio (name, shares, price, total, symbol, id) VALUES(:name, :shares, :price, :total, :symbol, :id)", name=stock["name"], shares=shares, price=usd(stock["price"]), total=usd(shares * stock["price"]), symbol=stock["symbol"], id=session["user_id"])
        # Else increment the shares count
        else:
            sharesTotal = userShares[0]["shares"] + shares
            db.execute("UPDATE portfolio SET shares=:shares WHERE id=:id AND symbol=:symbol", shares=shares_total, id=session["user_id"], symbol=stock["symbol"])

        # Return the index
        return render_template(url_for("index"))


@app.route("/history")
@login_required
def history():
    """Show history of transactions."""
    return apology("TODO")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""

    # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        # ensure username exists and password is correct
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["hash"]):
            return apology("invalid username and/or password")

        # remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # redirect user to home page
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method = "POST":
        rows = lookup(request.form.get("symbol"))

        if not rows:
            return apology("Invalid Symbol")

        return render_template("quoted.html", stock=rows)

    # Else, from GET 
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user."""

    if request.method == "POST":
        
        # Ensure user was submitted
        if not request.form.get("username"):
            return apology("Must provide Username.")

        # Ensure password was submitted
        elif not request.form.get("password0"):
            return apology("Must provide Password.")

        # Ensure both password are the same
        elif request.form.get("password0") != request.form.get("password1"):
            return apology("Password Doesn't Match.")

        # Insert the user into DB && store password hash
        dbInsert = db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)", username=request.form.get("username"), hash=pwd_context.encrypt(request.form.get("password"))
        
        # if use already exist
        if not dbInsert:
            return apology("Username Already exist.")

        # now, log the user directly
        session["user_id"] = dbInsert

        # and then redirect user to the home page
        return redirect(url_for("index"))
    
    # Else if user was redirected (get from GET request)
    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock."""

    if request.method == "GET":
        return render_template("sell.html")

    # else from post so, I'll check the symbols and shares
    else:
        stock = lookup(request.form.get("symbol"))
        if not stock:
            return apology("Invalid Symbol")

        # ensure proper number of shares
        try:
            shares = int(request.form.get("shares"))
            if shares < 0:
                return apology("Shares must be positive number.")
        except:
            return apology("Shares must be positive number.")

        # select the symbol shares of that user
        userShares = db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)", username=request.form.get("username"), hash=pwd_context.encrypt(request.form.get("password")))

        # Check if enough shares to sell
        if not userShares or int(userShares[0]["shares"]) < shares:
            return apology("Not Enough Shares")

        # Update history of a sell
        db.execute("INSERT INTO histories (symbol, shares, price, id) VALUES(:symbol, :shares, :price, :id)", symbol=stock["symbol"], shares=-shares, price=usd(stock["price"]), id=session["user_id"])

        # Update user cash (+)
        db.execute("UPDATE users SET cash = cash + :purchase WHERE id = :id", id=session["user_id"], purchase=stock["price"] * float(shares))

        # Update user shares (-)
        sharesTotal = userShares[0]["shares"] - shares

        # If shares comes to ZERO, delete it
        if sharesTotal == 0:
            db.execute("DELETE FROM portfolio WHERE id=:id AND symbol=:symbol", id=session["user_id"], symbol=stock["symbol"])
        # Else update the shares count
        else:
            db.execute("UPDATE portfolio SET shares=:shares WHERE id=:id AND symbol=:symbol", shares=shares_total, id=session["user_id"], symbol=stock["symbol"])

        # Return to index
        return redirect(url_for("index"))


@app.route("/history")
@login_required
def hostory():
    """Show history of interactions / transactions"""

    histories = db.execute("SELECT * FROM histories WHERE id=:id", id=session["user_id"])

    return render_template("history.html", histories=histories)


@app.route("/loan")
@login_required
def loan():
    """Get A Loan."""

    if request.method == "POST":

        # Ensure the proper usage (integers)
        try:
            loan = int(request.form.get("loan"))
            if loan < 0:
                return apology("loan must be positive amount.")
            elif loan > 9999:
                return apology("Can Not Loan more that 9999 :) ")
        except:
            return apology("Loan must be positive Integer")
    
        # Update User Cash (+)
        db.execute("UPDATE user SET cash = cash + :loan WHERE id=:id", loan=loan, id=session["user_id"])

        # Return to index
        return redirect(url_for(index))
    
    # From GET
    else:
        return render_template("loan.html")
