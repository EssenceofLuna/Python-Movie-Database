import sqlite3
from sqlite3 import Error

# This script is for me to learn sqlite3 in Python to create a database

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print("error: "+str(e))
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_connection("testdatabase.db")