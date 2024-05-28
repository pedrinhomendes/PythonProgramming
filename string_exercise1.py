# 1
message = "Hello, World!"
print(message[0])
print(message[len(message)-1])

# 2
str = "Python Programming"
substr = str[:6]
print(substr)
substrs = str[7:]
print(substrs)

# 3
message = "hello, world!"
l = message.upper()
print(l)

r = message.replace("world", "Python")
print(r)

# 4
print("Hello" + " " + "World")

# 5
fruits = ("apple,banana,cherry")
print(fruits.split(","))

# 6
name = "Leo"
age = 6

formatted_spring = f"My name is {name} and I am {age} years old"

print(formatted_spring)

# 7
user_string = input("Enter a string: ")
print(user_string[::-1])