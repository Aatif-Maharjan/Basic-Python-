#Write a Python program that determines whether a given string is a palindrome or not.
string=input("Enter a string: ")
rstring=string.reverse()
if(string == rstring):
    print(f"{string} is an palindrome string.")
else:
    print(f"{string} is not an palindrome string.")