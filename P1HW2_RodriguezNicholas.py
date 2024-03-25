# Nicholas Rodriguez

# 23 Feb. 2024

# P1HW2

# Creating travel itinerary and expenses based on user input

print('This program calculates and displays travel expenses')
print() # emptyline

budget = int(input('Enter Budget: '))
print() # emptyline

my_loc = str(input('Enter your travel destination: '))
print() #emptyline

_gas = int(input('How much do you think you will spend on gas? '))
print() # emptyline

lodge = int(input('Approximately, how much will you need for accomodation/hotel? '))
print() # emptyline

eat = int(input('Last, how much do you need for food? '))
print() # emptyline

title = 'Travel Expenses'
line = '-' * len(title)
print(line + title + line)

print(f'Location: {my_loc}')
print(f'Initial Budget: {budget}')
print() # emptyline

print(f'Fuel: {_gas}')
print(f'Accomodation: {lodge}')
print(f'Food: {eat}')
print() # emptyline
print(line + line + line)

print(f'Remaining Balance: {budget - _gas - lodge - eat}')

'''
Let budget be represented by an integer input from user.

For my_loc, it will return a string input from user of their destination of travel.

_gas, lodge, and eat will be integers from user input.

Once all fields are completed, a remaining balance will be represented by the difference of the budget, subtracted by the _gas, lodge, and eat amounts and all inputs will be listed. 
'''
