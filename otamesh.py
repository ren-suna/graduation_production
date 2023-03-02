# flaskモジュールをつかえるように
from flask import Flask
from flask import render_template
from flask import redirect
import sqlite3
from flask import request,session
# flaskを使うときのお約束
app = Flask(__name__)

app.secret_key = 'sunabaco'


@app.route("/top")
def top():

    return render_template("M_top.html")

@app.route("/right")
def right():
    return render_template("R.main_right.html")

@app.route("/regist_top")
def regist_top():
    return render_template("M.signup.html")

@app.route("/rooms")
def rooms():
    return render_template("H_madorizuadd.html")
    
@app.route("/furnitures")
def furnitures():
    return render_template("M.edit.html")


@app.route("/r_regist")
def r_regist():
    return render_template("H_sunpouadd.html")

@app.route("/save_s")
def main_right():
    conn=sqlite3.connect('graduate.db')
    # カーソル生成
    c=conn.cursor()
    # SQLを実行
    user_id = session['user_id']
    c.execute('select * from my_furnitutes where USER_ID=?',(user_id,))
    # Pythonで受け取る
    py_fu=c.fetchall()
    print(py_fu)
    # DBセッション終了
    conn.close()

    return render_template("R.main.html",furnitutes=py_fu)


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
    
    return render_template("M_top.html")


# 以下ログイン
@app.route("/login", methods=["POST"])
def login_post():
    conn = sqlite3.connect('graduate.db')
    p1 = request.form.get('post_pass')
    p2 = request.form.get('post_id')

    session["pass"]= p1
    session["id"]= p2

    c = conn.cursor()
    
    c.execute('SELECT * FROM users WHERE password = ? and USER_ID = ?',(p1,p2))
    result = c.fetchall()
    session["user_id"] = result[0][0]
    if result == []:
        return redirect("/top")
    else:
        print("ログインに成功しました")
   
    # conn.close()
    # return render_template("R.main.html", name=result[0][1])

    user_id = session['user_id']
    c.execute('select * from my_furnitutes where USER_ID=?',(user_id,))
    # Pythonで受け取る
    py_fu=c.fetchall()
    # DBセッション終了
    conn.close()

    return render_template("R.main.html", name=result[0][1],furnitutes=py_fu)



# 以下マイページへの遷移
@app.route("/header_top", methods=["GET"])
def header_top():
    conn = sqlite3.connect('graduate.db')
    c = conn.cursor()

    c.execute('SELECT * FROM users WHERE password = ? and USER_ID = ?',(session["pass"],session["id"]))
    result = c.fetchall()

    user_id = session['user_id']
    c.execute('select * from my_furnitutes where USER_ID=?',(user_id,))
    # Pythonで受け取る
    py_fu=c.fetchall()
    # DBセッション終了
    conn.close()

    return render_template("R.main.html", name=result[0][1],furnitutes=py_fu)

# @app.route('/main')
# def main():
#     conn = sqlite3.connect('graduate.db')
#     c = conn.cursor()
#     c.execute('SELECT * FROM users WHERE name')
#     result = c.fetchall()
#     py_name = int(result)



# 以下家具編集
@app.route("/edit_f")
def edit_f():
    print(session['user_id'])
    return render_template("M.edit.html")




@app.route("/regist_f", methods=["POST"])
def furniture():
    conn = sqlite3.connect('graduate.db')
    v1 = request.form.get('f_name')
    v2 = request.form.get('f_vertical')
    v3 = request.form.get('f_horizontal')
    v4 = request.form.get('f_height')
    v5 = request.form.get('f_quantity')
    c = conn.cursor()

    c.execute('INSERT INTO my_furnitutes (USER_ID,furniture_name,furniture_vertical,furniture_horizontal,furniture_height,furniture_quantity) VALUES (?,?,?,?,?,?)', (session['user_id'],v1,v2,v3,v4,v5,))
    #↓押し込む場合はcommit  py_task = c.fetchall()←引っ張ってくる場合はfetchall
    conn.commit()
    conn.close()
    
    return redirect("/header_top")




# ↑上は起動してる
# 以下メモとして使用


# @app.route("/add" ,methods=["POST"])
# def add():
#     conn = sqlite3.connect('graduate.db')
#     v1 = request.form.get('post_task')
#     v2 = request.form.get('post_add')
#     c = conn.cursor()
    
#     c.execute('INSERT INTO users (tasks,deadline) VALUES (?,?)', (v1,v2))
#     #↓押し込む場合はcommit  py_task = c.fetchall()←引っ張ってくる場合はfetchall
#     conn.commit()
#     conn.close()
#     return redirect("/top")



# @app.route("/delete" ,methods=["POST"])
# def delete():
#     conn = sqlite3.connect('DB.db')
#     c = conn.cursor()

#     v1 = request.form.get('post_id')

#     c.execute('DELETE FROM todo WHERE ID=?',(v1,))
#     conn.commit()
#     conn.close()
#     return redirect("/top")


# @app.route("/update" ,methods=["POST"])
# def update():
#     conn = sqlite3.connect('DB.db')
#     c = conn.cursor()

#     v1 = request.form.get('post_up')

#     c.execute('UPDATE todo SET delete = "1" WHERE  id = ?',(v1,))
#     conn.commit()
#     conn.close()
#     return "成功！"


if __name__ =="__main__":
    app.run(debug=True,port=9000)