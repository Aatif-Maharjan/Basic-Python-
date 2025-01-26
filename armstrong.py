print("Program for Armstrong")
n =int(input("Enter a Number: "))
a=n
b=a
number_of_digits=0
for i in range(10):
    if (n>=1):
        n=n/10
        number_of_digits += 1
print(f"The number has {number_of_digits} digits.")

power= number_of_digits
x=0
for j in range(power+1):
    x=a%10
    x=x+x^(power)
    a=a/10
if (b==x):
    print(f"{b} is armstrong.")
else:
    print(f"{b} is not armstrong.")
        