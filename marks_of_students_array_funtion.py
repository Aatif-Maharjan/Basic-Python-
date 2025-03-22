def marks_of_students():
    average = 0
    sum = 0
    n=[]
    print('ENter marks of ten students.')
    for i in range(0,10):
        marks=int(input(f"enter your marks of {i+1}: "))
        sum += marks
    average = sum /10
    return sum,average

x,y=marks_of_students()
print("The sum is",x,"The average:",y)
    