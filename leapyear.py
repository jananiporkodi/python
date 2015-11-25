year1 = input("Year 1?")
year2 = input("Year 2?")
year = range(int(year1), int(year2))
for x in year:
    if ((x % 4) == 0):
        if (x % 100 == 0):
            if (x % 400 == 0):
                print(x)
            else:
                pass
        else:
            print(x)
    else:
        pass
