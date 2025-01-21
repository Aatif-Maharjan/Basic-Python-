#include <stdio.h>

int main() {
    int num,sum=0;

    printf("Enter numbers one at a time. Enter 0 to end the program.\n");
    while (1) 
    {
        printf("Enter a number: ");
        scanf("%d",&num);

        if (num == 0) 
        {
            break;
        }

        if (num % 2 == 0) 
        {
            sum += num;
        }
    }

    printf("Sum of all even numbers entered: %d\n",sum);
    return 0;
}
