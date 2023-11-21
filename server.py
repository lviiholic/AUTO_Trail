from flask import Flask, render_template, request
import sqlite3
import markdown

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    conn = sqlite3.connect('data/hiking.db')
    cursor = conn.cursor()
    cursor.execute('SELECT t.trail_name FROM Trail t')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    if request.method == 'POST':
        my_select = request.form['trails']
        print(my_select)
        conn = sqlite3.connect('data/hiking.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT t.trail_name, p.park_name, t.region, t.difficulty, t.length, t.time, t.star
            FROM Trail t
            JOIN Park p ON t.park_id = p.park_id
            WHERE t.trail_name = ?
        """,(my_select,))
        row = cursor.fetchone()
        conn.close()

        result = "Trail Name: {}\n".format(row[0])+"Park Name:{}\n".format(row[1])+"Region:{}\n".format(row[2])+"Difficulty:{} star(s)\n".format(row[3])+"Length:{} Km\n".format(row[4])+"Duration:{} hour(s)\n".format(row[5])+"Recommanded:{} star(s)\n".format(row[6])

        return render_template('index.html', rows=rows, result=result)
    else:
        return render_template('index.html', rows=rows)


@app.route('/result', methods=['POST'])
def result():
    input_data = request.form['input_data']
    # Call your Python program here
    output_data = 'Hello, ' + input_data + '!'
    return render_template('result.html', output_data=output_data)

if __name__ == '__main__':
    app.run(debug=True)
