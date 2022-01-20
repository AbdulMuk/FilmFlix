from searchFilms import *

def searchMenu():
    
    while True:
        print("\nSearch Options")
        print("1. Search by film title")
        print("2. Search by genre")
        print("3. Search by year of release")
        print("4. Search by rating")
        print("5. Back to Menu Options")
        
        options = input("\nEnter one of the options above: ")
        
        if options == "1":
            searchFilm("title")
        elif options == "2":
            searchFilm("genre")
        elif options == "3":
            searchFilm("yearReleased")
        elif options == "4":
            searchFilm("rating")
        elif options == "5":
            break
        
        if options not in ["1","2","3","4","5"]:
            print("Choice not in the list of options available")