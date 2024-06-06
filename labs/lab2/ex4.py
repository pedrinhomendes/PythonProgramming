library = {"978-3-16-148410-0": {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
 "978-0-14-028329-7": {"title": "1984", "author": "George Orwell", "year": 1949},
 "978-0-7432-7356-5": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
 "978-0-452-28423-4": {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}}

# 1


for bookid, details in library.items():
    id = bookid
    title = details["title"]
    author = details["author"]
    year = details["year"]

    print(f"ID: {id}, Title: {title.capitalize()}, Author: {author.capitalize()}, Year: {year}")

# 2

third_key = list(library.keys())[2]
third_element_details = library[third_key]

print(f"ISBN: {third_key}")
print(f"Title: {third_element_details['title']}")
print(f"Author: {third_element_details['author']}")
print(f"Year: {third_element_details['year']}")

# 3

library["978-1-4028-9462-6"] = {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}
print(library)

# 4

library["978-0-7432-7356-5"] = {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1961}
print(library)

# 5

removed = library.pop("978-0-452-28423-4")
print(library)