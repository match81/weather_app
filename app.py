from flask import Flask

# Flaskアプリの本体を作成
app = Flask(__name__)

# ルートURL ("/") にアクセスがあったときに実行される関数を定義
@app.route('/')
def home():
    return "天気予報アプリへようこそ！"

# このファイルが直接実行された場合にのみ、Webサーバーを起動
if __name__ == '__main__':
    app.run(debug=True)