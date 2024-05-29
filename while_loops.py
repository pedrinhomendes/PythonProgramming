# While loop
# - to repeat a block of code

# syntax (structure)
#   code to repeat

# 1. iterate a range of numbers
# To get the sum of 1 to 10
i = 1                #start with a variable
sum = 0
while i <= 10:
    if i % 2 == 0:
        sum += i
    i += 1

print(sum)
# 2. iterate a sequence of characters (string)
# Count the number of vowels in a string
city = "Vancouver"
i = 0
count_vowels = 0
while i < len(city):
    if city[i] in "AEIOUaeiou":
        count_vowels += 1
    i += 1

print(f"the number of vowels in {city} is {count_vowels}.")

# 3. iterate a sequence of any data elements (list)
# print either english or french speaking provinces
provinces = ["AB", "BC", "ON", "QB", "SK", "PR"]
i = 0
while i < len(provinces):
    if provinces[i] in ["AB", "BC", "ON", "SK"]:
        print(f"{provinces[i]} speaks English.")
    elif provinces[i] == "QB" or provinces[i] == "PR":
        print(f"{provinces[i]} speaks French.")
    i += 1



# 3. iterate a sequence of any data elements (list)
