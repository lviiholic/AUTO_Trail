from flask import Flask, render_template
import markdown

app = Flask(__name__)

@app.route('/')
def index():
    # 读取Markdown文件内容
    with open('example.md', 'r', encoding='utf-8') as f:
        md_content = f.read()
    # 使用Python-Markdown库将Markdown转换为HTML
    html_content = markdown.markdown(md_content)
    # 将HTML内容传递给模板
    return render_template('index.html', content=html_content)
