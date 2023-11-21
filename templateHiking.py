import sqlite3
from sqlite3 import Error
import pandas as pd

def templateAny(templateIndex):
    try:
        conn = sqlite3.connect('data/hiking.db')
    except Error as e:
        print(e)
        
    cursor = conn.cursor()

    # 执行 SQL
    cursor.execute("""
        SELECT template, sql_text
        FROM Template
        WHERE template_id = ?
    """,(templateIndex,))
    row = cursor.fetchone()
    tText = row[0]
    Ta = tText.split()
    Fin = ""
    vIndex = 0
    for word in Ta:
        if word[0]=='{' :
            Fin = Fin + " "+ str(vA[vIndex])
            vIndex = vIndex + 1
        else:
            Fin = Fin +" "+ word
    return Fin;