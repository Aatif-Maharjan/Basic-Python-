sentence=input("Enter a string. ")
word= sentence.split()
print(word)
for i in word:
   # longest_word = max(word, key=len)  
   print(i)
   longest_word = max(word,key=len)
print(f"The longest word is: {longest_word}." )