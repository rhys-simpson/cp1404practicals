"""
CP1404 Practical - Extension
Gopher Population Simulator

Rhys Simpson
"""

import random

print("Welcome to the Gopher Population Simulator")
gopher_starting_population = 1000
print("Starting population: {}".format(gopher_starting_population))
MIN_INCREASE = 0.1
MAX_INCREASE = 0.2
MIN_DECREASE = 0.05
MAX_DECREASE = 0.25

population = gopher_starting_population
year = 1
print("Year {}\n".format(year))

while year <= 9:
    population_increase = 0
    population_decrease = 0
    year += 1

    percentage_increase = random.uniform(MIN_INCREASE, MAX_INCREASE)
    population_increase += (population * percentage_increase)
    percentage_decrease = random.uniform(MIN_DECREASE, MAX_DECREASE)
    population_decrease += (population * percentage_decrease)
    population_change = population_increase - population_decrease
    print("{:,.0f} gophers were born. {:,.0f} died.".format(population_increase, population_decrease))

    population += population_change
    print("Population: {:,.0f}".format(population))
    print("Year: {}\n".format(year))
