v=str(input("Enter a string: "))
list="aeiouAEIOU"
count=0
for i in v:
    if (i in list):
        count= count + 1
print(f"The number of vowels in string is {count}.")
