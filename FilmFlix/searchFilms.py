from dbConnection import *

def searchFilm(field):

    if field == "title":
        searchMsg = "Enter the films title: "
    elif field == "yearReleased":
        searchMsg = "Enter the films year of release: "
    elif field == "rating":
        searchMsg = "Enter the rating of the films: "
    elif field == "genre":
        searchMsg = "Enter the genre of the films: "

    searchVal = input(searchMsg).title()

    cursor.execute('SELECT * FROM tblFilms WHERE ' +  field + ' like '+"'%" + searchVal + "%'")
    
    row = cursor.fetchall()
    for record in row:
        print(record)
    
    input("\nPress any key to continue. ")