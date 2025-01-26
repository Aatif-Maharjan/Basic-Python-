a=[15,17,19,30,7]
i=0
j=1
max=a[1]
while i<5:
    while j<=4:
        if a[i]>a[j]:
            max= a[i]
        j=j+1
    i+=1
print(f"Max bumber is {max}")   
        