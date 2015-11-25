a = [4, 5, 6]
b = sorted(set(a))
if (len(b) > 1):
    print(b[-2])
else:
    print(b[0])
