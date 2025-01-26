a=[60,67,45,87,90,78,84,38,13,56]
i=0
sum=0
number_of_student=0
while i<len(a):
    if a[i]>=60:
        number_of_student+=1
        sum = sum +a[i]   
    if a[i]==13:
        print("Yes student has scored exactly 13.")
    i+=1
print(f"{number_of_student} has scored 60 and above.sum of their marks is {sum}")