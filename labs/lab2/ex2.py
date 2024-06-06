inventory = {"apple": (50, 0.5),
 "banana": (100, 0.2),
 "orange": (75, 0.3),
 "pear": (20, 0.4)}

# 1.

print("Current Inventory:")

for item, (quantity, price) in inventory.items():
    print(f"Item: {item.capitalize()}, Quantity: {quantity}, Price ${price:.2f} each")

# 2.

total_value = 0
for item, (quantity, price) in inventory.items():
    total_value += quantity * price

print(f"The total value of the inventory is {total_value}")

# 3.

inventory["mango"] = (30, 0.6)
print(inventory)

# 4.

inventory["banana"] = (120, 0.2)
print(inventory)


# 5.

del inventory["pear"]
print(inventory)