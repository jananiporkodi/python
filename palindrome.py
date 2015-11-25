def palindrome(str):
    i=0
    while i<len(str):
        if str[i]==str[-1-i]:
            i+=1
            return True
        return False

c= palindrome('madam')
if(c):
    print ('It is a Palindrome')
else:
    print ('It is not a Palindrome')


