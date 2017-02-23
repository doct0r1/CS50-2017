/**
 * helpers.c
 *
 * Helper functions for Problem Set 3.
 * Author: Mustafa Jamal
 */
 
#include <cs50.h>

#include "helpers.h"

/**
 * Returns true if value is in array of n values, else false.
 */
bool search(int value, int values[], int n)
{
    // TODO: implement a searching algorithm
   bool found = false;
    int low = 0; 
    int high = n - 1;
    
    //loop
    while (high >= low)
    {
        int mid = (low + high) / 2;
        if (value < values[mid])
            high = mid - 1;
        else if (value > values[mid])
            low = mid + 1;
        else
        {
            found = true;
            break;
        }
    }
    return value;
}

/**
 * Sorts array of n values.
 */
void sort(int values[], int n)
{
    // TODO: implement an O(n^2) sorting algorithm
        // Selection Sort Algorithm

    int i, steps, temp;
    for (steps = 0; steps < n; steps++)
    for (i = steps + 1; i < n; i++)
    {
        if (values[steps] > values[i])
        {
            temp = values[steps];
            values[steps] = values[i];
            values[i] = temp;
        }
    }
    return;
}
