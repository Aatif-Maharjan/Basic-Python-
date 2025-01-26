marks=[60,67,45,87,90,78,84,38,13,56]
number_of_students=0
sum_of_marks=0
for i in marks:
    if(i>=60):
        number_of_students +=1
        sum_of_marks +=i
    elif(i==13):
        print("Yes student has scored exactly 13.")
print(f"{number_of_students} scored exactly 60 or more than 60.")
print(f"{sum_of_marks} is the total marks scored by the number of students.")