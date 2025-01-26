name=input("ENter a string: ")
i=0
while i<len(name):
    if name[i]=="AEIOUaeiou":
        print(f"{name[i]} is vowel.")
    elif name[i]==" ":
        break
    else:
        print(f"{name[i]} is consonant.")
    i+=1