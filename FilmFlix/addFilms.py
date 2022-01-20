from dbConnection import *
import time

def addFilms():
    films = []

    print("\nAdd a film\n")
    title = input("Enter the film title: ")
    year = input("Enter year released: ")
    rating = input("Enter the film rating: ")
    duration = input("Enter the film duration: ")
    genre = input("Enter the genre of the film: ")

    films.append(title)
    films.append(year)
    films.append(rating)
    films.append(duration)
    films.append(genre)

    try:
        year = int(year)
        duration = int(duration)
    except:
        print("\nYear released and duration has to be a number")
        print(f"The Film {title} has not added!")
        input("\nPress any key to continue. ")
        return

    try:
        cursor.execute('INSERT INTO tblFilms VALUES (NULL, ?, ?, ?, ?, ?)', films)
        conn.commit()
        print(f"\nFilm {title} has been added")

        time.sleep(2)
        cursor.execute('SELECT * FROM tblFilms')
        row = cursor.fetchall()
        for record in row:
            print(record)
    except:
        print(f"\nThe Film {title} has not added!")
    
    input("\nPress any key to continue. ")