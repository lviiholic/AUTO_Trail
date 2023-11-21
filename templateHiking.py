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
        SELECT template, sql_text
        FROM Template
        WHERE template_id = ?
    """,(templateIndex,))
    row = cursor.fetchone()
    tText = row[0]
    Ta = tText.split()
    
    cursor.execute(row[1])
    Fin = ""
    vIndex = 0
    for word in Ta:
        if word[0]=='{' :
            print(word)
            print(vA[vIndex])
            Fin = Fin + " "+ str(vA[vIndex])
            vIndex = vIndex + 1
        else:
            Fin = Fin +" "+ word
    return Fin;

def getVa(index):
    try:
        conn = sqlite3.connect('data/hiking.db')
    except Error as e:
        print(e)
        
    cursor = conn.cursor()
    cursor.execute("""
        SELECT template, sql_text
        FROM Template
        WHERE template_id = ?
    """,(index,))
    row = cursor.fetchone()
    sqlText = row[1]
    cursor.execute(sqlText)
    row = cursor.fetchall()
    return row