# leap year debugging:
year =  int(input("enter the year which you want to check: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is leap yr")
        else:
            print(f"{year} is not leap yr")
    else:
        print(f"{year} is leap yr")
else:
    print(f"{year} is not leap yr")