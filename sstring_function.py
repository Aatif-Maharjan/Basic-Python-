def string_function(naam):
    return naam[::-1]

name='jhilke'
print("Outside function, now we call function")
returned_name=string_function(name)
print("The reverse of",name,"is",returned_name)