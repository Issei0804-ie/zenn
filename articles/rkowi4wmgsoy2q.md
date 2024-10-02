---
title: "Laravel v11.0.4 まとめ"
emoji: "📘"
type: "tech"
topics:
  - "php"
  - "laravel11"
published: true
---

30minで読めるだけ読んだので、全部のリリースはまとめきれてないこともあります。
リリースノートは[こちら](https://github.com/laravel/framework/releases/tag/v11.0.4)

- [11.x] Add class_exists check for `Spark`'s `subscribed` default alias Middleware by @akr4m in #50489
- [11.x] Fix: Removed TTY mode to resolve Windows compatibility issue  by @yourchocomate in #50495
- [11.x] Check for password before storing hash in session by @valorin in #50507
- [11.x] Fix an issue with missing controller class by @driesvints in #50505
- [11.x] Add default empty config when creating repository within CacheManager by @noefleury in #50510


### [11.x] Add class_exists check for `Spark`'s `subscribed` default alias Middleware by @akr4m in #50489

Laravelのデフォルトの依存関係にSparkが入っていないにも関わらず、デフォルトでSparkのミドルウェアを見つけ出そうとするためクラスが見つからずエラーが出ていたらしい。Sparkのミドルウェアが見つかる時のみ、middlewareのaliasに登録してくれるっぽいです。

### [11.x] Fix: Removed TTY mode to resolve Windows compatibility issue  by @yourchocomate in #50495


Windowsだとttyモードが使えないっぽいので、Windowsの時はttyをfalseにするらしい。

ttyについて、
> TTY mode connects the input and output of the process to the input and output of your program,

なので、僕のイメージ的には今実行しているプロセスの標準入出力新しく立ち上げる標準入出力に繋げるみたいなイメージです。

公式に[サンプルコード](https://laravel.com/docs/11.x/processes#tty-mode)があります。

```
Process::forever()->tty()->run('vim');
```

ちなみになぜWindowsだとttyモードが使えないかについてはわからず...

### [11.x] Check for password before storing hash in session by @valorin in #50507

パスワードを使っていないユーザーを使用するとエラーが投げられるらしい。
ログアウト時にエラーが発生するっぽいが、そもそもどうやったらパスワード無しで認証ができるのかわからなかった...

### [11.x] Fix an issue with missing controller class by @driesvints in #50505

Laravel11からは基底のControllerが無くてもartisanコマンドからコントローラーを作成できるべきだが、エラーが表示され作成できないというissueがあった。

再現方法は下記らしいです。
1. 新たにLaravel11のアプリを準備する
2. 基底コントローラーを消す
3. artisanコマンドを使用して新しいコントローラーを作る

修正前はこんな感じで基底コントローラーの存在の確認をしていたらしく、
```
$baseControllerExists = class_exists($rootNamespace.'Http\Controllers\Controller');
```
これだと、基底コントローラーを消してもautoloadには残るのでバグが発生する感じです。

修正後はファイルがあるかどうか直接確認していました。

### [11.x] Add default empty config when creating repository within CacheManager by @noefleury in #50510

Laravel11のCacheManagerのrepositoryメソッドの引数が1つ増えた。

```
public function repository(Store $store, array $config) // 第二引数が増えたっぽい
```

これだと$configに何か値をつっこまないとそもそも動かない。
それをマイグレーションガイドに書く必要がある？というissueだったが、結局は第二引数にデフォルト値を取るように設定してPRを出していた。

PRではこんな感じで第二引数のデフォルト値が設定された。
```
public function repository(Store $store, array $config = [])
```

