def max_among_three(x,y,z):
    if a>b and a>c:
        return (a,"is the greatest among three.")
    elif b>a and b>c:
        return (b,"is the greatest among three.")
    else:
        return (c+ "is the greatest among three.")

a=10
b=11
c=18
print(max_among_three(a,b,c))