# Nicholas Rodriguez

# 24 Mar 2024

# P3HW2

# Program takes user input and displays name, hours worked, and pay rate. As well as overtime pay, hours, and gross pay

name = str(input("Enter employee's name: "))
wrkhr = int(input("Enter number of hours worked: "))
payr8 = float(input("Enter employee's pay rate: "))
line = '-' * 12
print(line + line + line)
print(f'Employee name:   {name}')

print('')
print("Hours Worked   Pay Rate    OverTime    OverTime Pay      RegHour Pay      Gross Pay")
print(line * 8)

if wrkhr >=40:
    ovr_wrk = wrkhr - 40
    reg_wrk = 40
else:
    ovr_wrk = 0
    reg_wrk = wrkhr

ovrtime_pay = 0
if ovr_wrk > 0:
    ovrtime_pay = ovr_wrk * (payr8 * 1.5)

reg_pay = reg_wrk * payr8
grs_pay = reg_pay + ovrtime_pay
    
print(f'{wrkhr:<15.1f}{payr8:<12.1f}{ovr_wrk:<12.1f}{ovrtime_pay:<18.2f}${reg_pay:<16.2f}${grs_pay:<13.2f}')

'''
Program takes User input in the fields.

Let name be an input string, wrkhr is amount of hours worked as input intger,

and payr8 is floating point integer input.

Utilizing if-else branches, program calculates overtime hours and overtime pay.

As well as regular pay and gross pay. Calculations and inputs will display.
'''


