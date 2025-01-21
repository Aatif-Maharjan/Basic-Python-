#include <stdio.h>

void multiplication_table(int n, int i) 
{
    if (i>10)  
        return;
    printf("%d x %d = %d\n",n,i,n*i);
    multiplication_table(n,i+1);  
}

int main() 
{
    int n;
    printf("Enter a number to generate multiplication table: ");
    scanf("%d", &n);
    multiplication_table(n,1);  
    return 0;
}
