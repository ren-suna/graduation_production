# flaskモジュールをつかえるように
from flask import Flask
from flask import render_template
from flask import redirect
import sqlite3,os
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
    print(p1)
    print(p2)
    # 以下未完成
    c.execute('SELECT * FROM users WHERE password = ? and USER_ID = ?',(p1,p2))
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

    c.execute('select * from my_furnitutes where USER_ID=? and furniture_name IS NOT NULL',(user_id,))
    # Pythonで受け取る
    py_fu=c.fetchall()
    print(py_fu)

    c.execute('select * from my_furnitutes where USER_ID=? and room_name IS NOT NULL',(user_id,))
    py_room=c.fetchall()
    print(py_room)

    # roompass = py_fu[0][8].replace("\\","/")
    # print(roompass)
    # print(py_fu)
    # print(py_fu[0][8])
    # DBセッション終了
    conn.close()

    return render_template("R.main.html", name=result[0][1],furnitutes=py_fu,room=py_room)



# 以下マイページへの遷移
@app.route("/header_top", methods=["GET"])
def header_top():
    conn = sqlite3.connect('graduate.db')
    c = conn.cursor()
    print(session["pass"])
    c.execute('SELECT * FROM users WHERE password = ? and USER_ID = ?',(session["pass"],session["id"]))
    result = c.fetchall()

    user_id = session['user_id']

    c.execute('select * from my_furnitutes where USER_ID=? and furniture_name IS NOT NULL',(user_id,))
    # Pythonで受け取る
    py_fu=c.fetchall()
    print(py_fu)

    c.execute('select * from my_furnitutes where USER_ID=? and room_name IS NOT NULL',(user_id,))
    py_room=c.fetchall()
    print(py_room)

    # DBセッション終了
    conn.close()

    return render_template("R.main.html", name=result[0][1],furnitutes=py_fu,room=py_room)

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
    
    print(v1)
    print(session['user_id'])

    c.execute('INSERT INTO my_furnitutes (USER_ID,furniture_name,furniture_vertical,furniture_horizontal,furniture_height,furniture_quantity) VALUES (?,?,?,?,?,?)', (session['user_id'],v1,v2,v3,v4,v5,))
    #↓押し込む場合はcommit  py_task = c.fetchall()←引っ張ってくる場合はfetchall
    conn.commit()
    conn.close()
    
    return redirect("/header_top")


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
    c.execute('update my_furnitutes set furniture_name=? ,furniture_vertical=? ,furniture_horizontal=? ,furniture_height=? ,furniture_quantity=? where ID=? and USER_ID=?' ,(v1,v2,v3,v4,v5,py_id,user_id))

    print(py_id)

    #↓押し込む場合はcommit  py_task = c.fetchall()←引っ張ってくる場合はfetchall
    conn.commit()
    # DBセッション終了
    conn.close()

    return redirect("/header_top")


    # 家具削除-------------------
@app.route("/delete" ,methods=["POST"])
def delete():
    conn = sqlite3.connect('graduate.db')
    
    c = conn.cursor()
    # # SQLを実行
    py_id=request.form.get('post_id')
    user_id = session['user_id']

    # print(f_id)
    print(py_id)
    print(user_id)

    c.execute('DELETE from my_furnitutes where ID=? and USER_ID=? ',(py_id,user_id,))
    # Pythonで書きこみ決定させる
    conn.commit()
    # DBセッション終了
    conn.close()

    return redirect("/header_top")


    # 部屋削除-------------------
@app.route("/delete_room" ,methods=["POST"])
def delete_r():
    conn = sqlite3.connect('graduate.db')
    
    c = conn.cursor()
    # # SQLを実行
    room_id=request.form.get('room_id')
    user_id = session['user_id']

    # print(f_id)
    print(room_id)
    print(user_id)

    c.execute('DELETE from my_furnitutes where ID=? and USER_ID=? ',(room_id,user_id,))
    # Pythonで書きこみ決定させる
    conn.commit()
    # DBセッション終了
    conn.close()

    return redirect("/header_top")

# 画像をアップロードするよ
@app.route('/upload', methods=["POST"])
def do_upload():
    upload = request.files['upload']
    save_path = get_save_path()
    filename = upload.filename
    test = os.path.join(save_path,filename)
    test2 = test.replace('\\','/')
    print(test2)
    upload.save(os.path.join(save_path,filename))

    user_id = session['user_id']
    # user_id = 133
    conn = sqlite3.connect('graduate.db')
    c = conn.cursor()
    # 上記の filename 変数ここで使うよ
    c.execute("INSERT INTO my_furnitutes (USER_ID,room_name,room_picture) VALUES(?,?,?)",(user_id,filename,test2))
    conn.commit()
    conn.close()
    return redirect("/header_top")

def get_save_path():
    path_dir = "static\img"
    return path_dir



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