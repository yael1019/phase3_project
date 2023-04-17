import sqlite3

CONN = sqlite3.connect('lib/db/development.db')
CURSOR = CONN.cursor()
