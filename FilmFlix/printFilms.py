from dbConnection import *

def printFilms():
    cursor.execute('SELECT * FROM tblFilms')
    row = cursor.fetchall()
    for record in row:
        print(record)
    
    input("\nPress any key to continue. ")