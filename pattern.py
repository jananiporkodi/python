def patternA(n):
    for i in range(0, n):
        for j in range(0, i):
            print(j+1, end='')
        print('')

patternA(7)

print('')

def patternB(n):
    for i in range(n, 1, -1):
        for j in range(1, i):
            print(j, end='')
        print('')

patternB(7)

print('')

def patternC(n):
    for i in range (n, 0, -1):
        for j in range(i-1, 0, -1):
             print(j, end='')
        print('')

patternC(7)

print('')

def patternD(n):
    for i in range (n, 0, -1):
        for j in range (n-i):
            print (' ', end = '')
        for j in range (i-1):
            print (j+1, end = '')
        print()

patternD(7)

