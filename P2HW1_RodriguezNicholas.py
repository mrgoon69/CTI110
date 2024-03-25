# Nicholas Rodriguez

# 23 Feb. 2024

# P1HW2

# Creating travel itinerary and expenses based on user input

print('This program calculates and displays travel expenses')
print() # emptyline

budget = float(input('Enter Budget: '))
budget_str = f'${budget:.2f}'
print() # emptyline

my_loc = str(input('Enter your travel destination: '))
print() #emptyline

_gas = float(input('How much do you think you will spend on gas? '))
_gas_str = f'${_gas:.2f}'
print() # emptyline

lodge = float(input('Approximately, how much will you need for accomodation/hotel? '))
lodge_str = f'${lodge:.2f}'
print() # emptyline

eat = float(input('Last, how much do you need for food? '))
eat_str = f'${eat:.2f}'
print() # emptyline

title = 'Travel Expenses'
line = '-' * len(title)
print(line + title + line)

print(f'Location: {my_loc.rjust(24)}')
print (f'Initial Budget: {budget_str.rjust(19)}')
print(f'Fuel: {_gas_str.rjust(28)}')
print(f'Accomodation: {lodge_str.rjust(20)}')
print(f'Food: ${eat_str.rjust(27)}')
print(line + line + line)
print() # emptyline

balance_str = f'${budget - _gas - lodge - eat:.2f}'
print(f'Remaining Balance: {balance_str.rjust(15)}')

'''
Let budget be represented by an integer input from user.

For my_loc, it will return a string input from user of their destination of travel.

_gas, lodge, and eat will be integers from user input.

Once all fields are completed, a remaining balance will be represented by the difference of the budget, subtracted by the _gas, lodge, and eat amounts and all inputs will be listed. 
'''
