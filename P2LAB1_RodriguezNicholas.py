#Nicholas Rodriguez

#03 Mar. 2024

#P2LAB1

#Program calculates cost of distances when user inputs gas mileage and gas cost(cost per gallon)

your_gasmileage = float(input( ))
your_gascost = float(input( ))

cost_distance1 = 20 * (your_gascost/ your_gasmileage)
cost_distance2 = 75 * (your_gascost/ your_gasmileage)
cost_distance3 = 500 * (your_gascost/ your_gasmileage)

print(f'{cost_distance1:.2f} {cost_distance2:.2f} {cost_distance3:.2f}')
