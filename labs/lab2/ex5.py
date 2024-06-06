cities = {"New York": 8419000,
 "Los Angeles": 3980000,
 "Chicago": 2716000,
 "Houston": 2328000,
 "Phoenix": 1690000}

# 1

for item,(population) in cities.items():
    print(f"Item: {item.capitalize()}, Population: {population}")

# 2

highest_pop_city = max(cities, key=cities.get)
highest_pop = cities[highest_pop_city]


print(f"The highest population city is {highest_pop_city} with a population of {highest_pop}")

# 3

lowest_pop_city = min(cities, key=cities.get)
lowest_pop = cities[lowest_pop_city]

print(f"The lowest population city is {lowest_pop_city} with a population of {lowest_pop}")

# 4

cities["Phoenix"] = 1700000
print(cities)


# 5

cities["San Francisco"] = 884000
print(cities)