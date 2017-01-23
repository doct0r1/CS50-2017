/*
 This is CS50 less comforatable
CS50 pset2
Author: Mustafa Jamal
*/

#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    // get the user name
    string s = get_string();
    
    if (s !=(NULL))
    {
        //print the first letter in upper case
        printf("%c", toupper(s[0]));
    
        //check the rest of the name
        // using for loop
        for (int i = 0, n = strlen(s); i < n; i++)
        {
            //check spaces
            if (s[i] == ' '  && s[i++] != '\0')
            {
                //print the rest of the initials and increment
                printf("%c", toupper(s[i++]));
                i++;
            }
        }
        printf("\n");   //printing new line 
    }
}
