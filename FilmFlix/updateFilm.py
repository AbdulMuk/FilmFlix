from dbConnection import *
import time

def updateFilm():
    print("\nUpdate a film's records\n")
    idField = input("Enter ID of film to be updated: ")
    fieldName = input("Which field do you want to update: (1. title, 2. yearReleased, 3. rating, 4. duration, 5. genre) ")
    newFieldValue = input("Enter the new value for the field you are updating: ")

    if fieldName == "1":
        fieldName = "title"
    elif fieldName == "2":
        fieldName = "yearReleased"
    elif fieldName == "3":
        fieldName = "rating"
    elif fieldName == "4":
        fieldName = "duration"
    elif fieldName == "5":
        fieldName = "genre"
    
    if fieldName in ["2", "yearReleased", "4", "duration"]:
        try:
            newFieldValue = int(newFieldValue)
        except:
            print("\nYear released and duration has to be a number")
            print(f"Film {idField} has not been updated!")
            input("\nPress any key to continue. ")
            return

    newFieldValue = "'" + str(newFieldValue) + "'"

    try:
        cursor.execute("UPDATE tblFilms SET " + fieldName + "=" + newFieldValue + " WHERE filmID=" + idField)
        conn.commit()
        print(f"\nFilm {idField} has been updated")
        
        time.sleep(2)
        cursor.execute("SELECT * FROM tblFilms WHERE filmID=" + idField)
        row = cursor.fetchall()
        for record in row:
            print(record)
    except:
        print(f"\nFilm {idField} has not been updated!")

    input("\nPress any key to continue. ")