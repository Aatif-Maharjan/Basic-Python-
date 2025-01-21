'''name="""HELLO
this multi line 
string hahaha!!!"""
print(type(name)) #type - check the type of a variable
print(len(name)) #len - check the length of string'''

#index - both positive and negative index exist 
'''name="rambahadur"
print(name[2])
print(name[-4])
print(name[2:5])
print(name[-5:-3])
print(name[:3])
print(name[4:])
print(name[::-1])#reverse string
#print(name[start:end:step size])
print(name[1:8:3])
print(name[6::-2])'''

name="RaM baHadUr"
print(name.capitalize())
print(name.title())
print(name.upper())
print(name.lower())

n1="rambahadur"
print(n1.islower())
print(n1.isupper())
print(n1.swapcase())
print(n1.startswith('r'))
print(name.startswith('rA'))
print(name.endswith('r'))
print(name.endswith("dur"))


nam="My name is anthony gonje"

print(nam.split('a'))
print(nam.split('a',1))

list=["my","name","is","marybiscuit"]
print(" ".join(list))
print("!@".join(list))

hehe="rameshlal"
mint="gaurav_0"
print(hehe.index('m'))
print(hehe.find('m'))
print(hehe.index('a'))
print(hehe.rindex('a')) #gives the index of the character which is in the right side
print(hehe.find('a'))
print(hehe.rfind('a'))
#print(hehe.index('c'))
print(hehe.find('c'))
print(hehe.replace('r','c'))
print(mint.replace('0','gay'))
print(hehe.count('a'))