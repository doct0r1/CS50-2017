#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    //declare variables 
    float dolla;
    int num;             //store dolla $ value
    int counter = 0;     //with counting form 0

    do
    {
        printf("O hai! How much change is owed? \n");
        dolla = get_float();
    }
    while(dolla < 0);

    //convert dolla to int
    num =  round (dolla * 100);

    //first is  quarters
    while (num >= 25)
    {
        counter++;
        num = num - 25; 
    }

    //second is Dimes
    while (num >= 10)
    {
        counter++;
        num = num - 10;
    }

    //third is nickels
    while (num >= 5)
    {
        counter++;
        num = num - 5;
    }

    //fourth is pennies
    while (num >= 1)
    {
        counter++;
        num = num - 1;
    }
    printf("%d\n" ,counter + num );
    return 0;
}
