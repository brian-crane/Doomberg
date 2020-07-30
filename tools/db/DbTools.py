#This file contains operations needed to interact with my DB
import psycopg2
from tools.other import Tools

debug = True
sounds = True
# Init connection with DB
conn = psycopg2.connect(database="Doomberg", user="postgres",password="postgres", host="127.0.0.1")
if debug: print("Connected to DB!")

# Run one query on the DB
def executeQuery(query):
    if debug: print("Executing query: " + query.replace("VALUES","\n\tVALUES"))
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    try:
        records = cur.fetchall()
    except psycopg2.ProgrammingError:
        if sounds: Tools.playLowBeep()
        return None
    if sounds: Tools.playHighBeep()
    return records

def closeConnection():
    conn.close()
    if debug: print("PostgresSQL Connection has been closed")
