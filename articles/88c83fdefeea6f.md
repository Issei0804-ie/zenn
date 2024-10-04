---
title: "Laravel v11.0.2 まとめ"
emoji: "📘"
type: "tech"
topics:
  - "php"
  - "laravel"
  - "laravel11"
published: true
published_at: "2024-09-30 23:23"
---

30minで読めるだけ読んだので、全部のリリースはまとめきれてないこともあります。

リリースノートは[こちら](https://github.com/laravel/framework/releases/tag/v11.0.2)

- [11.x] Adds --graceful to php artisan migrate by @nunomaduro in #50486

migrateコマンドでエラーが出ても正常終了コードを返すようにするオプション(いつ使うんだ)
あとなんでgracefulというoption名なのかわからないので、英語わかる方教えてください。

今回は1件しかないのでちょっと深読みしてみる。

migrateコマンドの中に、`ConfirmableTrait`というtraitが存在したので中身を見てみる。

https://github.com/laravel/framework/blob/11.x/src/Illuminate/Console/ConfirmableTrait.php#L18

ある条件を満たした時に`Are you sure you want to run this command?`みたいな確認をしてくれる機能らしい。
デフォルトでは本番環境の時にこのメッセージが出るようになっているっぽい。
