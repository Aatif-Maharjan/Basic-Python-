#isoceleous traingle
a=int(input("Side 1: "))
b=int(input("Side 2: "))
c=int(input("Side 3: "))
if (a==b and b==c):
    print("It is an equlateral traiangle.")
elif (a==b and a!=c):
    print("It is an iscelous traingle.")
elif (a==c and a!=b):
    print("It is an isocelous traingle.")
elif (c==b and c!=a):
    print("It is an isocelous traingle.")