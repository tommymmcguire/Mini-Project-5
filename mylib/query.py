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


