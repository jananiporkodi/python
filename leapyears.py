def printLeapYrs( start, end):
    for year in (range(start, end)):
        if((year % 4 == 0) & ((year % 100 !=0) | (year % 400 == 0))):
            print(year)

printLeapYrs(1688, 2002)

