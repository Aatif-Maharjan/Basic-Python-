n=int(input("Enter a multi-digit number: "))
sum=0
while n!=0:
    a=n%10
    sum+=a
    n=n//10
print(f"The sum of multi-digit number is {sum}.")