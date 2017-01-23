/*
 This is CS50 more comforatable
pset2
Author: Mustafa Jamal
*/

#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    // user input
    string s = get_string();
    if (s != NULL)      //check input is not NULL
    {
        //boolean expression check any word in string and it be false when there's no words
        bool s_start = false;
        
        // iterate over the charcters
        for (int i = 0, n = strlen(s); i < n; i++)
        {
            char c = s[i];    //declare charcters form the string
            
            //check if the charcter (char) is the first letter in the word
            if (c != ' ' && s_start == false)
            {
                printf("%c", toupper(c));   //print the first char in Capital (upper case)
                s_start = true; 
            }
            
            //check the current word as ended or not 
            if (c == ' ')
            {
                s_start = false;
            }
        }
        printf("\n");       // printing new line
    }
    return 21;      // :P hahaha :D 
}
