from printFilms import *
from addFilms import *
from updateFilm import *
from deleteFilm import *
from searchMenu import *

def menuOptions():
    options = 0
    
    while options not in ["1","2","3","4","5","6"]:
        print("\nMenu Options")
        print("1. Add a film")
        print("2. Delete a film")
        print("3. Update a film's records")
        print("4. Print film details")
        print("5. Search for films")
        print("6. Exit")
        
        options = input("\nEnter one of the options above: ")
        if options not in ["1","2","3","4","5","6"]:
            print("Choice not in the list of options available")
    return options


while True:
    
    mainMenu = menuOptions()

    if mainMenu == "1":
        addFilms()
    elif mainMenu == "2":
        delFilm()
    elif mainMenu == "3":
        updateFilm()
    elif mainMenu == "4":
        printFilms()
    elif mainMenu == "5":
        searchMenu()
    else:
        break
