/**
 * generate.c
 *
 * Generates pseudorandom numbers in [0,MAX), one per line.
 *
 * Usage: generate n [s]
 *
 * where n is number of pseudorandom numbers to print
 * and s is an optional seed
 */
 
#define _XOPEN_SOURCE

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// set the limit of pseudo rundom numbers to 65536 - 1
#define LIMIT 65536

int main(int argc, string argv[])
{
    // Program accepts 2 || 3 commant line arguments 
    if (argc != 2 && argc != 3)
    {
        printf("Usage: ./generate n [s]\n");
        return 1;
    }

    // atoi(const char *str) converts string argument to integer(type int)
    // convert the number of pseudoramndam numbers to int 
    int n = atoi(argv[1]);

    // if command line has [s] seed value > convert the value to int and start iterating form it 
    if (argc == 3)
    {
        srand48((long) atoi(argv[2]));  // seeding drand48() by calling srand48() with the value of argv[2] argument
    }
    else
    {
        srand48((long) time(NULL));
    }

    // for loop to iterate through n number to generate the list of n pseudorandum numbers
    for (int i = 0; i < n; i++)
    {
        printf("%i\n", (int) (drand48() * LIMIT));
    }

    // success
    return 0;
}
