def readDate():
    print("Enter the date:")
    month= int(input("month:"))
    
    day= int(input("day:"))
    
    year= int(input("year:"))
    return(month, day, year)
date = readDate()
print(readDate())
(month, day, year) = readDate()
