/*
This function return a sort and search of an array [containg some values]
specified for pset3

Author: Mustafa Jamal
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
/*
Pseudocode:
function countingSort(array, min, max):
    count: array of (max - min + 1) elements
    initialize count with 0
    for each number in array do
        count[number - min] := count[number - min] + 1
    done
    z := 0
    for i from min to max do
        while ( count[i - min] > 0 ) do
            array[z] := i
            z := z+1
            count[i - min] := count[i - min] - 1
        done
    done
*/
#define MAX 65536
void sort(int values[], int n)
{
   // TODO: counting_sort Algorithm
   int range = 65536;
   int store[range + 1];
   int *sorted = malloc(n * sizeof *sorted);
   //if (sorted == NULL)
    //return NULL;

   for (int i = 0; i <= range; i++)
   {
       store[i] = 0;
   }
   for (int i = 0; i < n; i++)
   {
       sorted[i] = 0;
   }
   for (int j = 0; j < n; j++)
   {
       store[values[j]]++;
   }
   for (int i = 0; i < range; i++)
   {
       store[i] += store[i - 1];
   }
   for (int j = n - 1; j >= 0; j--)
   {
       sorted[store[values[j]]] = values[j];
       store[values[j]]--;
   }
   return;
}

/*
So I never say die, aim never untrue
I'm never so high as when I'm with you
And there isn't a fire, that I wouldn't walk through
My army of one is gonna fight for you
*/
