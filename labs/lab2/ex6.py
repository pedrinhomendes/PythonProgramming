movies = {"Inception": {"year": 2010, "rating": 8.8, "genre": "Sci Fi"},
 "The Godfather": {"year": 1972, "rating": 9.2, "genre": "Crime"},
 "The Dark Knight": {"year": 2008, "rating": 9.0, "genre": "Action"},
 "Pulp Fiction": {"year": 1994, "rating": 8.9, "genre": "Crime"},
 "Forrest Gump": {"year": 1994, "rating": 8.8, "genre": "Drama"}}

# 1
for movie, details in movies.items():
    title = movie
    year = details["year"]
    rating = details["rating"]
    genre = details["genre"]

    print(f"Movie: {movie.capitalize()},Year: {year}, Rating: {rating}, Genre: {genre.capitalize()}")

# 2

highest_rated_movie = max(movies, key=lambda movie: movies[movie]["rating"])

highest_rating = movies[highest_rated_movie]["rating"]
highest_rated_movie_details = movies[highest_rated_movie]

print(f"The highest-rated movie is '{highest_rated_movie}' with a rating of {highest_rating}.")

# 3

movies["The Matrix"] = {"year": 1999, "rating": 8.7, "Genre": "Sci fi"}
print(movies)

# 4

movies["Inception"].update({"rating": 9.0})
print(movies)

# 5

del movies["Pulp Fiction"]
print(movies)



