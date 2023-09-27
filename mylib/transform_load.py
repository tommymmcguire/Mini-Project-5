"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,ingred_FPro,avg_FPro_products,avg_distance_root,ingred_normalization_term,semantic_tree_name,semantic_tree_node
"""
import sqlite3
import csv
import os

#load the csv file and insert into a new sqlite3 database
def load(dataset="/workspaces/sqlite-lab-mcg/master/IMDB-Movie-Data.csv"):
    """"Transforms and Loads data into the local SQLite3 database"""

    #prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=''), delimiter=',')
    conn = sqlite3.connect('IMDB_Movie_Data.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS IMDB_Movie_Data")
    c.execute("CREATE TABLE IMDB_Movie_Data (rank, title, genre, description, director, actors, year, runtime minutes, rating, votes, revenue millions, metascore)")
    #insert
    c.executemany("INSERT INTO IMDB_Movie_Data VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", payload)
    conn.commit()
    conn.close()
    return "IMDB_Movie_Data.db"

