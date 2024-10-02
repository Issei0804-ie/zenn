import requests
import random
import string

version = input('release version: ')

body = f'''
---
title: "Laravel v{version} まとめ"
emoji: "📘"
type: "tech"
topics:
  - "php"
  - "laravel11"
published: false
---

30minで読めるだけ読んだので、全部のリリースはまとめきれてないこともあります。
リリースノートは[こちら](https://github.com/laravel/framework/releases/tag/v{version})
'''

# http request

url = f'https://api.github.com/repos/laravel/framework/releases/tags/v{version}'
response = requests.get(url)

if response.status_code == 200:
    release_data = response.json()
    release_body = release_data['body']

    # リリースノートから変更点を抽出し、先頭の * を - に変更
    changes = [line.strip().replace('*', '-', 1) for line in release_body.split('\n') if line.strip().startswith('*')]
    
    # 変更点を本文に追加
    for change in changes:
        body += f"\n{change}"
else:
    print(f"エラー: GitHubからデータを取得できませんでした。ステータスコード: {response.status_code}")

# slugは半角英数字（a-z0-9）、ハイフン（-）、アンダースコア（_）
def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))

random_string = generate_random_string(14)


# artiles以下にファイルに書き込み

with open(f'articles/{random_string}.md', 'x') as file:
    file.write(body)

