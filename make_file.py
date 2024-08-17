import os
from datetime import datetime

# 日付からファイル名を生成
file_name = datetime.now().strftime("%Y-%m-%d") + ".html"

# HTMLテンプレートの内容
content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Diary Entry</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>今日の日記</h1>
    <p>ここに日記の内容を書いてください。</p>
</body>
</html>
"""

# ファイルを作成し、内容を書き込む
with open(file_name, 'w',encoding='utf-8') as file:
    file.write(content)

print(f"{file_name} が作成されました。")
