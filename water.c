/*
created by: Mustafa Jamal 
CS50 pset1
*/

#include <stdio.h>
#include <cs50.h>

int main(void)

{
	// declare variables 
	int hi;
	int sp = 0;

	//do while loop
	do 
	{
		printf("height: ");
		hi = GetInt();
	}
	while ((hi < 0) || (hi > 23));

	//bui;ding the 2 pyramids
	for (int a = hi; a > 0; a--)
	{
		for (int b = 0; b< (a - 1); b++)
		{
			printf(" ");
		}
		printf("#");
		//sp++;
		for (int d = 0; d < sp; d++)
		{
		//	printf("#");
		}
		printf("\n");
	}
	return 0;
}
