#include <stdio.h>

int main(void)
{
    //declare variables
    int rows;
    int cols;
    int space;
    int num;

    //user intput
    printf("Height: ");
    scanf("%d", &num);

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
        cols++;
        printf("#");
        printf("\n");
    }
    //getch();
    return 0;
    
}
