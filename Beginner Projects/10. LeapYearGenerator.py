def century_leap_years(century):
    
    start_year = ((century-1)*100) + 1
    end_year = ((century-1)*100) + 100
    IsLeapYear = False

    while start_year <= end_year + 1:

        if IsLeapYear == False:
            if start_year % 4 == 0:
                IsLeapYear = True
            
        if IsLeapYear == True:
            print(f"Leap Year: {start_year}")
            start_year += 4
        else:
            start_year += 1

while True:
    print("Please enter the century you want to get list of leap years for (e.g 21)")
    try:
        century = int(input("> "))
    except:
        print("Not a valid number. Try again!")
    else:
        century_leap_years(century)
        break
