a="1"
for i in range(1,6):
    print(f"{a*i}")
    a=str(int(a)+1)
    
print(" ")
print(" ")

for i in range(1,6):
    print('*'*i)

print(" ")
print(" ")

for i in range(5,0,-1):
    print('*'*i)
    
print(" ")
print(" ")

for i in range(5,1):
    print(f' '*(4-i),'*'*(i))
    
for i in range(5,0,-1):
    print(f" "*(5-i),"*"*(i))
    
print(" ")
print(" ")
    
name="Aatif"
for i in range (1,len(name)+1):
    print(name[:i])
    
print(" ")
print(" ")

for i in range (len(name),0,-1):
    print(name[:i])
    
print(" ")
print(" ")

for i in range (1,len(name)+1):
    print(f" "*(len(name)-i),name[:i])
    
print("")
print(" ")

for i in range (len(name),0,-1):
    print(f" "*(len(name)-i),name[:i])
    