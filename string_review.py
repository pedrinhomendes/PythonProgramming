# String Review
# String - text, "a sequence of characters"

greeting = "Hello"

# len(str) - returns the number of characters
l = len(greeting)
print (l)

# indexing []
print(greeting[3])

# slicing [s:e] - to get a substring
print(greeting[2:4])

# string methods
city_data = "Vancouver,Burnaby,Coquitlam,Surrey,North Vancouver,West Vancouver"
cities = city_data.split(",")
print(cities)

updated_cities = city_data.replace("Surrey","Port Coquitlam")
print(updated_cities)

i = city_data.find("Coquitlam") # returns the index of the substring, otherwise -1(doesn't exist)
print(i)

