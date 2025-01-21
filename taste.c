

#include<stdio.h>

char encryption_block(char data[])
{
    int i;
    for (i=0;(i<100 && data[i]!='\0');i++)
    {
        if (data[i]==' ')
        {
            continue;
        }
        data[i]=data[i]+2;
    }
    printf("This is your encrypted message.\n%s\n",data);

}

char decryption_block(char data[])
{
    int j;
    for(j=0;(j<100 && data[j]!='\0');j++)
    {
        if (data[j]==' ')
        {
            continue;
        } 
        data[j]=data[j]-2;
    }
    printf("This is your decrypted message.\n%s\n",data);
}

void main()
{
    char message[100];
    int choice;

    printf("Enter a Top-Secret message: \n");
    fgets(message,100,stdin);
    printf("Choose your option\n");
    printf("1 : Encrytion\n");
    printf("2 : Decrytion\n");
    printf("Choose 1 or 2: ");
    scanf("%d",&choice);

    if (choice == 1) 
    {
        encryption_block(message);
    }
    else if(choice == 2) 
    {
        decryption_block(message);
    }
    else 
    {
        printf("Error \n");
    }
}
