from flask import Flask, render_template, request,jsonify
import sqlite3
from templateHiking import templateAny

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    conn = sqlite3.connect('data/hiking.db')
    cursor = conn.cursor()
    cursor.execute('SELECT t.trail_name FROM Trail t')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('index.html', rows=rows)
    
@app.route('/choose',methods = ['POST'])
def choose():
    value = request.form.get('new_value')

    conn = sqlite3.connect('data/hiking.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT t.trail_name, p.park_name, t.region, t.difficulty, t.length, t.time, t.gradient, t.surface, t.star, t.summary
        FROM Trail t
        JOIN Park p ON t.park_id = p.park_id
        WHERE t.trail_name = ?
    """,(value,))
    row = cursor.fetchone()
    conn.close()
    print(row)
    result = row
    rText = templateAny('TP01', row)
    return jsonify({"result": rText})

if __name__ == '__main__':
    app.run(debug=True)
