word = input("Enter the word?")
rev_str = (word[::-1])
if(word == rev_str):
    print("palindrome")
else:
    print("Not palindrome")
