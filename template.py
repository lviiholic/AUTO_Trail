import sqlite3
from sqlite3 import Error
import pandas as pd

def templateAny(templateIndex, vA):
    try:
        conn = sqlite3.connect('data/hiking.db')
    except Error as e:
        print(e)
        
    cursor = conn.cursor()

    # 执行 SQL
    cursor.execute("""
        SELECT template
        FROM Template
        WHERE template_id = ?
    """,(templateIndex,))
    row = cursor.fetchone()
    tText = row[0]
    Ta = tText.split()
    print(Ta)
    Fin = ""
    vIndex = 0
    for word in Ta:
        if word[0]=='{' :
            Fin = Fin + " " + vA[vIndex]
            vIndex = vIndex + 1
        else:
            Fin = Fin +" "+ word
    print(Fin)

templateAny('TP01', ['A Trail', 'B park', 'C region', '2', '2','10','3','2','2','afikehfuifh'])