import sqlite3
from sqlite3 import Error
import pandas as pd

try:
    conn = sqlite3.connect('data/hiking.db')
except Error as e:
    print(e)
    
cursor = conn.cursor()

# 执行 SQL
cursor.execute("""
    SELECT *
    FROM Template
""")
row = cursor.fetchall()

tText = row[0][1]
print(tText)
Ta = tText.split()
print(Ta)
Fin = ""
for word in Ta:
    if word[0]=='{' :
        Fin = Fin + ' wooohuuuu'
    else:
        Fin = Fin +" "+ word
print(Fin)