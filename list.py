        
def sum_recursive(a):
    return a[0] + sum_recursive(a[1:])

a = [3, 2, 1, 4, 5]
print(sum_recursive(a))  

