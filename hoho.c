#include <stdio.h>
#define PI 3.14  

void takeinput(float *r, float *h) 
{
    printf("Enter the radius of the cylinder: ");
    scanf("%f",&r);  
    printf("Enter the height of the cylinder: ");
    scanf("%f",&h);  
}

float calculate_volume(float r, float h) 
{
    return PI*r*r*h;  
}

void display_volume(float volume) 
{
    printf("The volume of the cylinder is: %f\n",volume);  
}

int main() 
{
    float radius,height,volume;
    takeinput(&radius,&height);
    volume=calculate_volume(radius, height);
    display_volume(volume);
    return 0;
}
