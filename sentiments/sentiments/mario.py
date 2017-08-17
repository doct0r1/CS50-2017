def main(n):
    assert n in range(1,24)
    for i in range(2,n+2):
        print (' '*(n+1-i), end='')
        print ('#'*i)

if __name__ == '__main__':
    while True:
        no_of_lines = int(input('Height: ').strip())
        if no_of_lines in range(1,24):
            break
    main(no_of_lines)
