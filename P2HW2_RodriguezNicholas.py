# Nicholas Rodriguez

# 06 Mar 2024

# P2HW2

# User inputs module grades and program calculates sum, average, highest and lowest grades

mod1 = float(input('Enter grade for Module 1: '))
mod2 = float(input('Enter grade for Module 2: '))
mod3 = float(input('Enter grade for Module 3: '))
mod4 = float(input('Enter grade for Module 4: '))
mod5 = float(input('Enter grade for Module 5: '))
mod6 = float(input('Enter grade for Module 6: '))
print() # emptyline

title = 'Results'

line = '-' * 12
print(line + title + line)

grades = [mod1,mod2,mod3,mod4,mod5,mod6]
grades.sort()
#sorts list alphanumerically
highest = grades[-1]
#negative indexing starts from end
lowest = grades [0]
#is always the first
total = sum(grades)
average = total / len(grades)

average_str = f'{average:.2f}'
lowest_str = f'{lowest:.1f}'
highest_str = f'{highest:.1f}'
total_str = f'{total:.1f}'

print(f'Lowest Grade: {lowest_str.rjust(9)}')
print(f'Highest Grade: {highest_str.rjust(8)}')
print(f'Sum of Grades: {total_str.rjust(9)}')
print(f'Average: {average_str.rjust(15)}')
print(line * 3)

'''
Prompts user to input grades for modules.
Program reads grades and sorts grades in numerical/ascending order.
Last element of list is displayed as highest grade.
First element of list is displayed as lowest grade.
Average grade is calculated and displayed.
Sum of grades is calculated and displayed.
'''

