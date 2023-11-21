from flask import Flask, render_template
import markdown

app = Flask(__name__)

@app.route('/')
def index():
    # 读取Markdown文件内容
    # 将HTML内容传递给模板
    return render_template('text.html')

app.run(debug=True)