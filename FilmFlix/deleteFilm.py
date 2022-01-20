from dbConnection import *
import time

def delFilm():
    print("\nDelete a film\n")
    idField = input("Enter ID of the film to be deleted: ")
    
    try:
        cursor.execute("DELETE FROM tblFilms WHERE filmID =" + idField)
        conn.commit()
        print("\nFilm " + idField + " deleted")
        
        time.sleep(2)
        cursor.execute('SELECT * FROM tblFilms')
        row = cursor.fetchall()
        for record in row:
            print(record)
    except:
        print("\nFilm " + idField + " has not been deleted!")
    
    input("\nPress any key to continue. ")