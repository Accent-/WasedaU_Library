# WasedaU_Library
早稲田大学図書館のWebページで使える有用なツールを置いていくものです

# 使い方
1. secret.jsonに学生番号とパスワードを入れて保存
2. 同じディレクトリに`wine.py`と`auto_extension.py`を保存する
3. 好きなものを実行

# 説明
- `auto_extension.py`：書籍の延長を自動で行う
- `wine.py`：ツール群
- `add_book_title_to_wunderlist.py`：借りている書籍からタイトルと返却日を取得し、wunderlistに登録
- `wunderpy.py`：wunderlistの投稿や削除を行えるようにモジュール化したもの
 
# 注意
wunderlistに投稿するためには、自分の使っているlistのIDを予め知らなければならない。よって、`wunderpy.py`の`show_list_id()`でまずはリストのIDを調べてください。

