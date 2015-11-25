name1 = input("What's your name? ")
name2 = input("What's the second name? ")
str = []
combined = name1 + name2
name1 = set(list(name1))
name2 = set(list(name2))
unique_chars = (name1 ^ name2)
for c in combined:
    if c in unique_chars:
        str.append(c)
    else:
        pass
count = len(str)
while (count > 4):
    count -= 3
print(['Friendship', 'Love', 'Affection', 'Marriage', 'Enemies'][count])
