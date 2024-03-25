#Nicholas Rodriguez

#3 Mar. 2024

#P2LAB2

#Program takes input integers and outputs product and average both as floating-point values and rounded values.
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

value = num1 + num2 + num3 + num4
value1 = value/4
value2 = num1 * num2 * num3 * num4
print(f'{value2:.0f} {value1:.0f}')
print(f'{value2:.3f} {value1:.3f}')