from flask import Flask, render_template, redirect,request,session
import os
import sqlite3
# CGIモジュールのインポート
from flask import request

app=Flask(__name__)

#flaskからHTMLを生成
@app.route("/")
def test():
    print(test)
    return render_template("H_madorizuadd.html")

    #Flask実行（ターミナルでflask実行できなかったので）
if __name__ =="__main__":
    app.run(debug=True) #エラーはいてね！（サーバーを毎回落とさなくていい）

@app.route('/upload', methods=["POST"])
def do_upload():
    upload = request.files['upload']
    save_path = get_save_path()
    filename = upload.filename
    upload.save(os.path.join(save_path,filename))

    user_id = session['USER_ID']
    conn = sqlite3.connect('graduate.db')
    c = conn.cursor()
    # update文
    # 上記の filename 変数ここで使うよ
    c.execute("INSERT INTO my_furnitutes (room_no,room_picture) VALUES (filename,join(save_path,filename))")
    conn.commit()
    conn.close()
    return redirect ('/H_madorizuadd')

def get_save_path():
    path_dir = ".static/img"
    return path_dir