members = [{"name": "Alice", "age": 25, "books_borrowed": ["1984", "To Kill a Mockingbird"]},
 {"name": "Bob", "age": 30, "books_borrowed": ["The Catcher in the Rye"]},
 {"name": "Charlie", "age": 22, "books_borrowed": ["Brave New World", "1984"]},
 {"name": "David", "age": 35, "books_borrowed": ["The Great Gatsby"]}]

# 1

for member in members:
    print(f"Name: {member['name']}, Age: {member['age']}")

# 2

for member in members:
    if member["name"] == "Charlie":
        print(f"books_borrowed by Charlie: {member['books_borrowed']}")
        break

# 3

new_member= {"name": "Eve", "age": 28, "books_borrowed":["Pride and Prejudice"]}
members.append(new_member)

for member in members:
    print(member)

# 4

for member in members:
    if member["name"] == "Bob":
        member["age"] = 31
        break

for member in members:
    print(member)

# 5

for member in members:
    if member["name"] == "David":
        members.remove(member)
        break

for member in members:
    print(member)


















