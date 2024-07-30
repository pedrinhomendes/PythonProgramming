
# 1

add = lambda x: x + 15
print(add(5))

# 2

multiplies_2 = lambda x, y: x * y
print(multiplies_2(5, 6))

# 3

square = lambda x: x ** 2
print (square(2))

# 4

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_nums = list(filter(lambda x: x % 2 != 0, nums))
print(odd_nums)

# 5

temp = [10, 15, 20, 25, 30, 35]
temps = list(map(lambda x: x * 1.8 + 32, temp))
print(temps)

# 6

numbs = lambda x, y: max(x, y)
print(numbs(4, 7))

# 7
from functools import reduce

elements = [1, 2, 3, 4, 5, 6]

print(reduce(lambda x, y: x * y, elements))

# 8

check = lambda x: x % 3 == 0
print(check(15))

# 9

area = lambda width, height: width * height
print(area(6, 8))

# 10

numeric = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
increment_nums = list(map(lambda x: x + 1, numeric))

print(increment_nums)

# 11

string_func = lambda str: len(str)
print(string_func("college"))

# 12

concate = lambda str1, str2: str1 + str2
print(concate("Van", "couver"))

# 13

list_num = [1, 2, 4, 6, 9, 13]

greater_5 = list(filter(lambda x: x > 5, list_num))
print(greater_5)

# 14

check_letter =  lambda str, letter: letter in str
print(check_letter("Baseball", "s"))

# 15
num_ = [2, 4, 6, 8, 9, 10]

double = list(map(lambda x: x * 2, num_))
print(double)

# 16

ispalindrome = lambda str: str == str[::-1]
print(ispalindrome("radar"))

# 17

elements2 = [(1,"Pedro"), (2,"Joao"), (3,"Amanda"), (4,"Lucas"), (5,"Carol")]

sort_algo = lambda l: l[1]

sorted_elements2 = sorted(elements2, key=sort_algo)
print(sorted_elements2)

# 18

words = ["python", "spark", "box", "read", "programming", "key"]

four = list(filter(lambda str: len(str) > 4, words))
print(four)

# 19

factorial = lambda n: reduce(lambda x, y: x * y, range(1, n + 1))
print(factorial(6))

# 20

people = [{'name': 'Alex', 'age': 27}, {'name': 'Bruno', 'age': 30}, {'name': 'Peter', 'age': 19}, {'name': 'Carlos', 'age': 22}]

sort_algo = lambda l: l['age']

sorted_people = sorted(people, key=sort_algo)
print(sorted_people)

# 21

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

flatten = lambda list: sum(nested_list, [])
print(flatten(nested_list))

# 22

vowels = lambda str: (sum(1 for char in str.lower() if char in 'aeiou'))
print(vowels('Programming'))

# 23

random_numbers = [1, 2, 3, 4, 5, 6]

second_largest = (lambda lst: sorted(set(lst), reverse=True)[1])(random_numbers)
print(second_largest)


# 24

numbers = [1, 2, 2, 3, 4, 4, 5]

duplicates = lambda numbers: list(dict.fromkeys(numbers))
print(duplicates(numbers))

# 25

word = ['Vancouver', 'Cornerstone', 'Downtown', 'Granville']

longest_word = lambda word: max(word, key=lambda word: len(word))
print(longest_word(word))