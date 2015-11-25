str = input("Enter the string?")
i = 0
for c in str:
    if (c in ('a', 'e', 'i', 'o', 'u')):
        i = i + 1
print(i)
