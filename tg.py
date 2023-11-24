import sqlite3
from sqlite3 import Error
try:
    conn = sqlite3.connect('data/hiking.db')
except Error as e:
    print(e)

cursor = conn.cursor()
#get tID input
tID = 'TP10000'
cursor.execute("""
    SELECT t.trail_name, p.park_name, t.region, t.difficulty, t.length, t.time, t.star
    FROM Trail t
    JOIN Park p ON t.park_id = p.park_id
    WHERE t.trail_id = ?
""",(tID,))
row = cursor.fetchone()
