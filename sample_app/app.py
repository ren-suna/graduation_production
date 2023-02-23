from flask import Flask
from flask import render_template
from flask import redirect
import random
import sqlite3

app = Flask(__name__)

@app.route("/test")
# /にアクセスしたら
def test():
   
    return render_template("base.html")
# index.htmlを使って　HTMLを生成





if __name__ == "__main__":
    app.run(debug=True,port=8080)