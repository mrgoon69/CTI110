# Nicholas Rodriguez

# 17 Mar 2024

# P3LAB

#Program determines leap year or not based on user input

is_leap_year = False

input_year = int(input())

if input_year % 4 == 0:
    if input_year % 100 == 0:
        if input_year % 400 == 0:
            is_leap_year = True
        else:
                is_leap_year = False
    else:
        is_leap_year = True

if is_leap_year:
            print(input_year,' - leap year')
else:
    print(input_year,' - not a leap year')
     
