#from moviefunctions import *
from moviefunctions_new import *

#add_movie(movieNameStr="boobs")
#listAllMovies()



add_movie("boobs", 8008, 69)
add_movie("tits", 420, 0)
add_movie("boobs", 8008, 0)
list_movies(True, True, True)

#main loop
while True:
    print("Enter menu...\n    1. Add movie\n    2. Update movie\n    3. List all movies")
    try:
        option=int(input())
    except:
        print("Error: invalid input")

    match option:
        case 1:
            print("Option 1")
            add_movie()
        case 2:
            print("Option 2")
        case 3:
            print("Option 3")
        case _:
            print("Invalid option selected")