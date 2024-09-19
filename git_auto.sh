#!/bin/bash

# 全ての変更をステージング
git add .

# コミットメッセージを引数として受け取り、コミットを作成
git commit -m "$1"

# リモートリポジトリにプッシュ
git push origin main