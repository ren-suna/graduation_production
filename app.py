from flask import Flask, render_template, redirect

import sqlite3
# CGIモジュールのインポート
from flask import request

app=Flask(__name__)

@app.route("/left1")
def left1():
    return render_template("R.main_left1.html")

@app.route("/left2")
def left2():
    return render_template("R.main_left2.html")

@app.route("/right")
def right():
    return render_template("R.main_right.html")

#flaskからHTMLを生成
@app.route("/")
def test():
    return render_template("R.main.html")




    #Flask実行（ターミナルでflask実行できなかったので）
if __name__ =="__main__":
    app.run(debug=True) #エラーはいてね！（サーバーを毎回落とさなくていい）
