# Nicholas Rodriguez

# 17 Mar 2024

# P3HW1

# User inputs module grades and program calculates sum, average, highest, lowest, and letter grade average

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))
print() #emptyline

# add grades entered to a list
title = 'Results'

line = '-' * 12
print(line + title + line)

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

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


# determine letter grade for average


if average >= 90:
    print('Your grade is: A')
elif average >= 80:
    print('Your grade is: B')
elif average >= 70:
    print('Your grade is: C')
elif average >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F') # TO DO: finish this





