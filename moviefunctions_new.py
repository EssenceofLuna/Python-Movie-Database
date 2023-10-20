import json

#TODO: put this in a better spot :3
movies = []

def add_movie(movieNameStr=None, length=None, rating=None, forceAppend=False):
    # Get movie name if one is not provided
    if movieNameStr == None:
        print("Enter movie name")
        movieNameStr = input()
    
    # Create object, replacing spaces with underscores and making lowercase, and retain the string as movieNameStr
    #movieObj = movieNameStr.replace(" ","_").lower()

    # get length if not provided
    if length == None:
        print("Enter movie length in seconds")
        length = input()

    # get rating if not provided
    if rating == None:
        print("Enter movie rating, 0-100")
        rating = input()

    movieListCheck = find_movie(movieNameStr)
    if forceAppend == True or movieListCheck == None:
        #add new move to list
        movies.append({
            "name": movieNameStr,
            "length": length,
            "rating": rating
        })
        #movies.append(movieObj)
    else:
        #if movie already exists, update its entry instead
        movies[movieListCheck] = {
            "name": movieNameStr,
            "length": length,
            "rating": rating
        }

def find_movie(movieName):
    for i in range(len(movies)):
        if movies[i].get("name") == movieName:
            return i
        print("DEBUG: movie found!!")
    print("DEBUG: Movie not found!!")
    #return False

def list_movies(names = True, lengths = False, ratings = False):
    for i in range(len(movies)):
        tempStr=""
        if names == True: tempStr += "Movie: "+movies[i].get("name")
        if lengths == True: tempStr += "\n    Length: "+str(movies[i].get("length"))
        if ratings == True: tempStr += "\n    rating: "+str(movies[i].get("rating"))
        print(tempStr)