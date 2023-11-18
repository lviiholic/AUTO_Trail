from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    input_data = request.form['input_data']
    # Call your Python program here
    output_data = 'Hello, ' + input_data + '!'
    return render_template('result.html', output_data=output_data)

if __name__ == '__main__':
    app.run(debug=True)
