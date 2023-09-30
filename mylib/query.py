"""Query the database"""

import sqlite3


def query():
    """Query the database for the top 5 rows of the IMDB-Movie-Data table"""
    conn = sqlite3.connect("IMDB_Movie_Data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM IMDB_Movie_Data")
    print("Top 5 rows of the IMDB_Movie_Data table:")
    print(cursor.fetchall())
    conn.close()
    return "Success"

def query_best():
    """Query the database for the best movies based on the genre"""
    movie_genre = input("Enter a movie genre: ")
    conn = sqlite3.connect("IMDB_Movie_Data.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT rating, metascore, title, genre, description, actors FROM IMDB_Movie_Data WHERE genre LIKE '%{movie_genre}%' ORDER BY rating DESC LIMIT 1")
    print(f"Best movie based on genre {movie_genre}:")
    print(cursor.fetchall())
    conn.close()
    return "Success"


