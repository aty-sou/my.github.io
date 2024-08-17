import os
from datetime import datetime

# 新しい日記ファイルの作成
date_str = datetime.now().strftime("%Y-%m-%d")
file_name = date_str + ".html"

content = f"""
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{date_str}の日記</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>{date_str}の日記</h1>
    <p>ここに日記の内容を書いてください。</p>
    <br>
    <a href="index.html">ホームに戻る</a>
</body>
</html>
"""

with open(file_name, 'w', encoding='utf-8') as file:
    file.write(content)

print(f"{file_name} が作成されました。")

# index.htmlにリンクを追加
index_file = "index.html"
new_link = f'<span class="section-title">日記</span><br>\n<a href="{file_name}">{datetime.now().strftime("%Y年%m月%d日")}</a>の日記<br>\n'

# index.htmlを読み込んでリンクを追加
if os.path.exists(index_file):
    with open(index_file, 'r', encoding='utf-8') as file:
        existing_content = file.read()

    # 新しいリンクを先頭に追加して保存
    updated_content = new_link + existing_content

    with open(index_file, 'w', encoding='utf-8') as file:
        file.write(updated_content)

    print(f"{index_file} にリンクが追加されました。")
else:
    print(f"{index_file} が見つかりませんでした。")
