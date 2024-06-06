countries = {"USA": "Washington, D.C.",
 "Canada": "Ottawa",
 "France": "Paris",
 "Germany": "Berlin",
 "Japan": "Tokyo"}

# 1

for country, capital in countries.items():
    print(f"Country: {country}, Capital: {capital}")

# 2

capital_of_germany = countries.get("Germany")
print(f"The capital of Germany is {capital_of_germany}.")

# 3

countries["Australia"] = "Canberra"
print(countries)

# 4

countries["USA"] = "New Washington, D.C."
print(countries)

# 5

del countries["France"]
print(countries)

