import sqlite3
import pandas as pd 

def initializedb():
    db = sqlite3.connect("./database.sqlite")

    with db:
        cur = db.cursor()
        cur.execute("DROP TABLE IF EXISTS data")
    
    return db

def read_db(db, number_rows=100):
    return pd.read_sql(f"SELECT * FROM data LIMIT {number_rows}", db)

def insert_row(db, df):
    df.to_sql("data",db, if_exists="append", index=True)


