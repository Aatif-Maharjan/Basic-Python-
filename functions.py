'''
with argument without return type
#chunck one
def add(c,d):
    print("This is inside the function")

haha=5
jeje=6 
print("This is outside the function.")
sum = add(haha,jeje)
'''


'''
#without argument but with return type
def with_return_type_but_without_argumnet():
    a=10
    b=11
    sum = a+b
    return sum

for i in range(with_return_type_but_without_argumnet()):
    print("jay nepal")
'''
 
'''   
def without_argument_and_return_type():
    a=int(input("ENter a numebr: "))
    b=int(input("ENter a numebr: "))
    print("This is the sum:",a+b)

without_argument_and_return_type()    
'''

def multiple_return_value():
    a=10
    b=8
    add=a+b
    diff=a-b
    return add,diff

x,y=multiple_return_value()
print("The sum is:",x)
print("The difference is:",y)