from flask import Flask, render_template, redirect

import sqlite3
# CGIモジュールのインポート
from flask import request

app=Flask(__name__)

#flaskからHTMLを生成
@app.route("/")
def test():
    print(test)
    return render_template("M_top.html")


    #Flask実行（ターミナルでflask実行できなかったので）
if __name__ =="__main__":
    app.run(debug=True) #エラーはいてね！（サーバーを毎回落とさなくていい）
