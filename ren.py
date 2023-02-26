import os
# splite3をimportする
import sqlite3
# flaskをimportしてflaskを使えるようにする
from flask import Flask , render_template , request , redirect , session
# appにFlaskを定義して使えるようにしています。Flask クラスのインスタンスを作って、 app という変数に代入しています。
app = Flask(__name__)

@app.route("/furnitures")
def furnitures():
    return render_template("M.edit.html")


@app.route("/right")
def main_right():
    conn=sqlite3.connect('graduate.db')
    # カーソル生成
    c=conn.cursor()
    # SQLを実行
    py_id="1"
    c.execute('select * from my_furnitutes where id=?',(py_id,))
    # Pythonで受け取る
    py_fu=c.fetchall()
    print(py_fu)
    # DBセッション終了
    conn.close()

    return render_template("R.main_right.html",furnitutes=py_fu)



@app.route("/delete")

def delete():
# DBから情報を取得して　変数py_taskに格納する
# DBとPythonを接続する
# import sqlite3　→　sqlite3.connect('example.db')

    conn=sqlite3.connect('graduate.db')
    # カーソル生成
    c=conn.cursor()
    # フォームデータを取得する
    v1=request.form.get('post_id')
    print(v1)
    # SQLを実行
    c.execute('DELETE from todo where id=?',(v1,))
    # Pythonで書きこみ決定させる
    conn.commit()
    # DBセッション終了
    conn.close()
    # HTMLに出力
    return redirect("/top")


# __name__ というのは、自動的に定義される変数で、現在のファイル(モジュール)名が入ります。 ファイルをスクリプトとして直接実行した場合、 __name__ は __main__ になります。
if __name__ == "__main__":
    # Flask が持っている開発用サーバーを、実行します。
    app.run( host='0.0.0.0', port=80 , debug=True)
