from imdb import IMDb,IMDbError
from imdb.Person import Person
import sys

# create an instance of the IMDb class
title = input("Enter movie name: ")
try:
    ia = IMDb()
    #Search for a particular movie
    movies = ia.search_movie(title)
    movie_id = movies[0].movieID

except:
    print("Movie unavailable")
    sys.exit(0)

movie = ia.get_movie(movie_id)
ia.update(movie,info=['vote details'])
title = movie['title']
print("Title: ",title)

def casting():
        
    try:
        cast = movie['cast']
    except:
        print("Cast details unavailable")
        sys.exit(0)
    print("Cast: ")
    for c in cast:
        print(c)

try:
    ratings = movie['median']
except:
    print("Ratings unavailable")
    casting()
print("Ratings: ",ratings)
casting()








