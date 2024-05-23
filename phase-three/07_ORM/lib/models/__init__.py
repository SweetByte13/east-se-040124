import sqlite3

# connect to DB
CONN = sqlite3.connect('development.db')
# communicate with DB
CURSOR = CONN.cursor()