# import json
import pickle

#TODO: find better place to create movies[]
movies = []

class Movie:
    name = ""
    genres = []
    length = 0 #in seconds
    rating = 0 # 0-100, with 10 being equivalent to 1.0

def save_movies():
    f = open('movies', 'wb')
    pickle.dump(movies, f)
    f.close()

    #print("DEBUG: movies saved")

def load_movies():
    f = open('movies', 'rb')
    loadedMovies = pickle.load(f)
    f.close()

    for i in loadedMovies:
        movies.append(i)

    #print("DEBUG: movies loaded")


def add_movie(movieNameStr=None, length=None, rating=None, load=True, save=True):
    # TODO: Verify input types

    # Get movie name if one is not provided
    if movieNameStr == None:
        print("Enter movie name")
        movieNameStr = input()
    
    # Create object, replacing spaces with underscores and making lowercase, and retain the string as movieNameStr
    movieObj = movieNameStr.replace(" ","_").lower()
    movieObj = Movie()
    movieObj.name = movieNameStr

    # get length if not provided
    if length == None:
        print("Enter movie length in seconds")
        movieObj.length = input()

    # get rating if not provided
    if rating == None:
        print("Enter movie rating, 0-100")
        movieObj.rating = input()

    if load == True: load_movies()

    #add movie to list of movies
    movies.append(movieObj)

    if save == True: save_movies()



def listAllMovies():
    for item in movies:
        print(item.name+" - length: "+item.length+" - rating: "+item.rating)
    #print("DEBUG: Listed movies")