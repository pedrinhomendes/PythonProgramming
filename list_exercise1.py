# 1
list = [1,2,3,4,5]
print(list[2])

# 2
list.append(6)
print(list)

list.pop(1)
print(list)

# 3
list_ = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(list_[:5])
print(list_[len(list_)-3:])
print(list_[::2])

# 4
listt = [1,2,3,4,5,6,7,8,9,10]
print(sum(listt))

print(max(listt), min(listt))

# 5
l = [i * i for i in range(1,11)] # multiple each value for itself
print(l)


# 6
numbers = [1, 2, 3], [4, 5, 6], [7, 8, 9]
print(numbers [1][1])


# 2

name_list = ['P', 'y', 't', 'h', 'o', 'n']
t = ''.join(name_list)
print(t)
