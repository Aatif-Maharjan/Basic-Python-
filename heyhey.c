#include <stdio.h>

int sum_of_natural_numbers(int n) 
{
    if (n == 1) 
    {
        return 1;
    } 
    else 
    {
        return n + sum_of_natural_numbers(n-1);
    }
}//aatif maharjan

int main() {
    int n;
    printf("Enter a positive integer: ");
    scanf("%d",&n);
    if (n>0) 
    {
        int result = sum_of_natural_numbers(n);
        printf("The sum of the first %d natural numbers is: %d\n",n,result);
    } 
    else 
    {
        printf("Please enter a positive integer.\n");
    }
    return 0;
}