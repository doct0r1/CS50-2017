// created by: Mustafa Jamal

#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //declare variables
    int rows;
    int cols;
    int space;
    int num;
    
    //user input 
    printf("Height: ");
    num = GetInt();
    
    //building pyramid 
    for (rows = 1; rows <= num; rows++)
    {
        for (space = 1; space <= (num - rows); space++)
        {
            printf(" ");
        }
        for (cols = 1; cols <= rows; cols++)
        {
            printf("#");
        }
        printf("  ");
        for (cols =1; cols <= rows; cols++)
        {
            printf("#");
        }
        printf("\n");
    }
    return 0;
}
