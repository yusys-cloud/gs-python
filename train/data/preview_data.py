import pandas as pd
from flask import Flask, render_template
dataset = pd.read_csv('/home/ubuntu/yzq/datasets/yu/js-codes.csv')
preview = dataset.head(100)  # 预览前10行数据
print(preview)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('preview.html', data=preview.to_html())

if __name__ == '__main__':
    app.run()