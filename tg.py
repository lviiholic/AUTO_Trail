import sqlite3
from sqlite3 import Error
import pandas as pd
conn = sqlite3.connect('data/hiking.db')
cursor = conn.cursor()
cursor.execute("""
    SELECT template
    FROM Template
    WHERE template_id = ?
""",('TP01',))
row = cursor.fetchone()
tText = row[0]
Ta = tText.split()
Fin = ""
vIndex = 0
for word in Ta:
    if word[0]=='{':
        print(word)
        vIndex = vIndex + 1
    else:
        Fin = Fin +" "+ word