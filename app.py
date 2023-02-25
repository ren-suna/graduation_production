# flaskモジュールをつかえるように
from flask import Flask
from flask import render_template
from flask import redirect
import sqlite3
from flask import request
# flaskを使うときのお約束
app = Flask(__name__)

@app.route("/top")
def top():

    return render_template("M_top.html")


@app.route("/regist_top")
def regist_top():
    return render_template("M.signup.html")

# 以下ユーザー登録
@app.route("/regist", methods=["POST"])
def regist_post():
    conn = sqlite3.connect('graduate.db')
    v1 = request.form.get('name')
    v2 = request.form.get('USER_ID')
    v3 = request.form.get('password')
    v4 = request.form.get('mailadress')
    c = conn.cursor()
   
    c.execute('INSERT INTO users (name,USER_ID,password,mailadress) VALUES (?,?,?,?)', (v1,v2,v3,v4))
    #↓押し込む場合はcommit  py_task = c.fetchall()←引っ張ってくる場合はfetchall
    conn.commit()
    conn.close()
    
    return render_template("R.main.html")

# 以下ログイン
@app.route("/login", methods=["POST"])
def login_post():
    conn = sqlite3.connect('graduate.db')
    v1 = request.form.get('post_id')
    v2 = request.form.get('post_pass')
    c = conn.cursor()
    print(v1)
    print(v2)
    # 以下未完成
    c.execute('SELECT * FROM users')
    c.fetchall()
    conn.close()

    return render_template("R.main.html")

@app.route("/login_l", methods=["POST"])
def login_post_l():
    return render_template("R.main_right.html")


# 以下家具編集
@app.route("/edit_f")
def edit_f():
    return render_template("M.edit.html")

@app.route("/regist_f", methods=["POST"])
def furniture():
    conn = sqlite3.connect('graduate.db')
    v1 = request.form.get('f_name')
    v2 = request.form.get('f_vertical')
    v3 = request.form.get('f_horizonrtal')
    v4 = request.form.get('f_height')
    c = conn.cursor()
    
    print(v1)

    c.execute('INSERT INTO my_furnitutes (furniture_name,furniture_vertical,furniture_horizontal,furniture_height) VALUES (?,?,?,?)', (v1,v2,v3,v4))
    #↓押し込む場合はcommit  py_task = c.fetchall()←引っ張ってくる場合はfetchall
    conn.commit()
    conn.close()
    
    return render_template("R.main.html")


if __name__ =="__main__":
    app.run(debug=True,port=9000)