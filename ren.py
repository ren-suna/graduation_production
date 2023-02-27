import os
# splite3をimportする
import sqlite3
# flaskをimportしてflaskを使えるようにする
from flask import Flask , render_template , request , redirect , session
# appにFlaskを定義して使えるようにしています。Flask クラスのインスタンスを作って、 app という変数に代入しています。
app = Flask(__name__)

# Flask では標準で Flask.secret_key を設定すると、sessionを使うことができます。この時、Flask では session の内容を署名付きで Cookie に保存します。
app.secret_key = 'sunabaco'


# @app.route("/right")
# def main_right():
#     conn=sqlite3.connect('graduate.db')
#     # カーソル生成
#     c=conn.cursor()
#     # SQLを実行
#     py_id="1"
#     c.execute('select * from my_furnitutes where id=?',(py_id,))
#     # Pythonで受け取る
#     py_fu=c.fetchall()
#     print(py_fu)
#     # DBセッション終了
#     conn.close()

#     return render_template("R.main_right.html",furnitutes=py_fu)

        c.close()
        return render_template('bbs.html' , user_info = user_info , comment_list = comment_list)
    else:
        return redirect("/top")


# __name__ というのは、自動的に定義される変数で、現在のファイル(モジュール)名が入ります。 ファイルをスクリプトとして直接実行した場合、 __name__ は __main__ になります。
if __name__ == "__main__":
    # Flask が持っている開発用サーバーを、実行します。
    app.run( host='0.0.0.0', port=80 , debug=False)
