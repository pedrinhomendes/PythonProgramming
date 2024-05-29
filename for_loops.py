# Loops: for loop, while loop
# - to repeat a block of code

# syntax (structure)
# for each_element(var) in iterables(collections)
#   code to repeat

# 1. iterate a range of numbers
# To get the sum of 1 to 10
sum = 0
for i in range(1, 11):
    if i % 2 == 0:  # %: remainder    to find sum of even numbers
        sum += i # sum = sum + 1

print(sum)

# 2. iterate a sequence of characters (string)
city = "Vancouver"
count_vowels = 0
for ch in city:
    if ch in "AEIOUaeiou":
        count_vowels += 1

print(f"the number of vowels in {city} is {count_vowels}.")

# 3. iterate a sequence of any data elements (list)
provinces = ["AB", "BC", "ON", "QB", "SK", "PR"]
for province in provinces:
    if province in ["AB", "BC", "ON", "SK"]:
        print(f"{province} speaks english")
    elif province == "QB" or province == "PR": # province in ["QB","PR"]
        print(f"{province} speaks french")

# 4.