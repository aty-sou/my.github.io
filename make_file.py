import os
from datetime import datetime

# ファイル名を決定するためのユーザー入力
def get_file_name():
    choice = input("ファイル名に日付を使いますか？ (y/n): ").strip().lower()
    if choice == 'y':
        return datetime.now().strftime("%Y-%m-%d") + ".html"
    elif choice == 'n':
        file_name = input("ファイル名を入力してください（拡張子は自動で追加されます）: ").strip()
        return file_name + ".html"
    else:
        print("無効な選択です。デフォルトで日付をファイル名にします。")
        return datetime.now().strftime("%Y-%m-%d") + ".html"

# ファイル名を決定
file_name = get_file_name()

# タイトルを決定
title = input("ページのタイトルを入力してください: ").strip()

# HTMLテンプレートの内容
content = f"""
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>{title}</h1>
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
new_link = f'<a href="{file_name}">{title}</a><br>\n'

if os.path.exists(index_file):
    with open(index_file, 'r', encoding='utf-8') as file:
        existing_content = file.read()

    # 日記セクションを特定し、新しいリンクをその後に追加
    start_tag = '<span class="section-title">日記</span><br>\n'
    start_index = existing_content.find(start_tag) + len(start_tag)
    
    if start_index != -1:
        # 既存のリンクの後に新しいリンクを追加
        before_links = existing_content[:start_index]
        after_links = existing_content[start_index:]
        
        # 新しいリンクを追加
        updated_content = before_links + new_link + after_links

        with open(index_file, 'w', encoding='utf-8') as file:
            file.write(updated_content)

        print(f"{index_file} にリンクが追加されました。")
    else:
        print(f"{index_file} 内に日記セクションが見つかりませんでした。")
else:
    print(f"{index_file} が見つかりませんでした。")
