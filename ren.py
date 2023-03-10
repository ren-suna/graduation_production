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
    v1 = request.form.get('post_pass')
    v2 = request.form.get('post_id')
    
    c = conn.cursor()
    print(v1)
    print(v2)
    c.execute('SELECT * FROM users WHERE password = ? and USER_ID = ?',(v1,v2))
    result = c.fetchall()
    print(result)
    session["user_id"] = result[0][0]
    if result == []:
        return redirect("/top")
    else:
        print("ログインに成功しました")
   
    print(session['user_id'])
    user_id = session['user_id']
    # user_id = 133
    c.execute('select * from my_furnitutes where USER_ID=?',(user_id,))
    # Pythonで受け取る
    py_fu=c.fetchall()
    # roompass = py_fu[0][8].replace("\\","/")
    # print(roompass)
    # print(py_fu)
    # print(py_fu[0][8])
    # DBセッション終了
    conn.close()

    return render_template("R.main.html", name=result[0][1],furnitutes=py_fu)


# 以下編集後メインに戻る → ×
@app.route("/tomain")
def tomain():
    conn = sqlite3.connect('graduate.db')
    # v1 = request.form.get('post_pass')
    # v2 = request.form.get('post_id')
    
    c = conn.cursor()
    # print(v1)
    # print(v2)
    c.execute('SELECT * FROM users WHERE ID = ?',(user_id,))
    result = c.fetchall()
    print(result)
    session["user_id"] = result[0][0]
    # if result == []:
    #     return redirect("/top")
    # else:
    #     print("ログインに成功しました")
   
    print(session['user_id'])
    # conn.close()
    # return render_template("R.main.html", name=result[0][1])

    # def main_right():
    # conn=sqlite3.connect('graduate.db')
    # # カーソル生成
    # c=conn.cursor()
    # # SQLを実行
    user_id = session['user_id']
    c.execute('select * from my_furnitutes where USER_ID=?',(user_id,))
    # Pythonで受け取る
    py_fu=c.fetchall()
    print(py_fu)
    # DBセッション終了
    conn.close()

    return render_template("R.main.html", name=result[0][1],furnitutes=py_fu)



# 以下家具編集
@app.route("/edit_f")
def edit_f():
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
    
    print(v1)

    c.execute('INSERT INTO my_furnitutes (furniture_name,furniture_vertical,furniture_horizontal,furniture_height,furniture_quantity) VALUES (?,?,?,?,?)', (v1,v2,v3,v4,v5))
    #↓押し込む場合はcommit  py_task = c.fetchall()←引っ張ってくる場合はfetchall
    conn.commit()
    conn.close()
    
    return render_template("R.main.html")

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

# ren.py追加
# @app.route("/right2")
# def main_right():
#     conn=sqlite3.connect('graduate.db')
#     # カーソル生成
#     c=conn.cursor()
#     # SQLを実行
#     user_id = session['user_id']
#     c.execute('select * from my_furnitutes where USER_ID=?',(user_id,))
#     # Pythonで受け取る
#     py_fu=c.fetchall()
#     print(py_fu)
#     # DBセッション終了
#     conn.close()

#     return render_template("R.main_right.html",furnitutes=py_fu)


# 家具編集画面へ遷移-------------------
@app.route("/UPDATE_fun" ,methods=["POST"])
def update():
    conn = sqlite3.connect('graduate.db')
    
    c = conn.cursor()
    # # SQLを実行
    py_id=request.form.get('post_id')
    user_id = session['user_id']

    # print(f_id)
    print(user_id)
    print(py_id)

    c.execute('select * from my_furnitutes where ID=? and USER_ID=? ',(py_id,user_id,))

    # Pythonで受け取る
    py_fu=c.fetchall()
    print(py_fu)
    # DBセッション終了
    conn.close()

    return render_template("R.edit_update.html", furnitutes=py_fu)


# 編集した家具情報をデータベースへUPDATE------------------
@app.route("/UPDATE_fun2", methods=["POST"])
def update2():
    conn = sqlite3.connect('graduate.db')
    v1 = request.form.get('name')
    v2 = request.form.get('f_vertical')
    v3 = request.form.get('f_horizontal')
    v4 = request.form.get('f_height')
    v5 = request.form.get('f_quantity')
    c = conn.cursor()
    
    print(v1)
    print(v2)

    user_id = session['user_id']
    py_id=request.form.get('post_id')
    # c.execute('UPDATE my_furnitutes (furniture_name,furniture_vertical,furniture_horizontal,furniture_height,furniture_quantity) VALUES (?,?,?,?,?)', (v1,v2,v3,v4,v5))  
    c.execute('update my_furnitutes set furniture_name=? ,furniture_vertical=? ,furniture_horizontal=? ,furniture_height=? ,furniture_quantity=? where ID=? and USER_ID=?' ,(v1,v2,v3,v4,v5,py_id,user_id))

    print(py_id)

    #↓押し込む場合はcommit  py_task = c.fetchall()←引っ張ってくる場合はfetchall
    conn.commit()

    # c.execute('SELECT * FROM users WHERE password = ? and USER_ID = ?',(v1,v2))
    # result = c.fetchall()

    # user_id = session['user_id']
    # c.execute('select * from my_furnitutes where USER_ID=?',(user_id,))
    # # Pythonで受け取る
    # py_fu=c.fetchall()
    # print(py_fu)
    # DBセッション終了
    conn.close()

    # return render_template("R.main.html")
    return redirect ('/UPDATE_fun2' ,methods=["POST"])


    # 家具削除-------------------
@app.route("/delete" ,methods=["POST"])
def delete():
    conn = sqlite3.connect('graduate.db')
    
    c = conn.cursor()
    # # SQLを実行
    py_id=request.form.get('post_id')
    user_id = session['user_id']

    # print(f_id)
    print(user_id)
    print(py_id)

    c.execute('delete from my_furnitutes where ID=? and USER_ID=? ',(py_id,user_id,))

    # Pythonで受け取る
    py_fu=c.fetchall()
    print(py_fu)
    # DBセッション終了
    conn.close()

    return render_template("R.edit_update.html", furnitutes=py_fu)



if __name__ =="__main__":
    app.run(debug=True,port=9000)