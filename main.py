# Flaskをインポート
from flask import Flask, render_template

# Flaskアプリを作成
app = Flask(__name__)

# エンドポイント'/'を設定
@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()