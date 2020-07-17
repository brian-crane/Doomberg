#This file contains operations needed to interact with my DB
import psycopg2

debug = True

# Init connection with DB
conn = psycopg2.connect(database="Doomberg", user="postgres",password="postgres", host="127.0.0.1")
if debug: print("Connected to DB!")

# Run one query on the DB
def executeQuery(query):
    if debug: print("Executing query: " + query)
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()

def closeConnection():
    conn.close()
    if debug: print("PostgresSQL Connection has been closed")
