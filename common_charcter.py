def union_function(x,y):
    p=set(a)
    q=set(b)
    v=p.intersection(q)
    return list(v)  

a=[12,4,6,7]
b=[7,9,0,11]
print(union_function(a,b))

def common_function(x,y):
    c=[]
    for i in x:
        if i in y:
            c.append(i)
    return c
   
a=[11,12,3,5,6]
b=[11,12,5,7,8] 
print(common_function(a,b))
    

#count the frequncey of character
def display(a,x):
    c=a.count(x)
    print(f"Given list has {c} no. of {x}")
    
a=[2,3,4,5,6,7,89,2,2,7]
x=7
display(a,x)


def display_char_frequency():
    string = input("Enter a string: ")
    counter=[]
    for i in string:
        if i not in counter:
            c=string.count(i)
            print(f"Number of {i} is {c}.")
            counter.append(i)

display_char_frequency()