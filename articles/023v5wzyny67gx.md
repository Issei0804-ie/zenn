---
title: "Laravel v11.0.6 まとめ"
emoji: "📘"
type: "tech"
topics:
  - "php"
  - "laravel"
  - "laravel11"
published: true
---

30minで読めるだけ読んだので、全部のリリースはまとめきれてないこともあります。
リリースノートは[こちら](https://github.com/laravel/framework/releases/tag/v11.0.6)

- [11.x] Fix version constraints for illuminate/process by @riesjart in https://github.com/laravel/framework/pull/50524
- [11.x] Update Broadcasting Install Command With Bun Support by @HDVinnie in https://github.com/laravel/framework/pull/50525
- [11.x] Allows to comment `web` and `health` routes by @nunomaduro in https://github.com/laravel/framework/pull/50533
- [11.x] Add generics for Arr::first() by @phh in https://github.com/laravel/framework/pull/50514
- Change default collation for MySQL by @driesvints in https://github.com/laravel/framework/pull/50555
- [11.x] Fixes install:broadcasting command by @joedixon in https://github.com/laravel/framework/pull/50550
- [11.x] Fix crash when configuration directory is non-existing by @buismaarten in https://github.com/laravel/framework/pull/50537


### [[11.x] Fix version constraints for illuminate/process by @riesjart](https://github.com/laravel/framework/pull/50524)

`Illuminate/Process`のcomposer.jsonがv10のまま更新されていなかったという話。

### [[11.x] Update Broadcasting Install Command With Bun Support by @HDVinnie](https://github.com/laravel/framework/pull/50525)

broadcast機能をインストールする時にbunでもインストールできるようにしたらしい。

### [[11.x] Allows to comment `web` and `health` routes by @nunomaduro](https://github.com/laravel/framework/pull/50533)


`app.php`にて、web,health,api,pagesなどが含まれていないときに例外を投げる仕様を修正したらしい。

```php
return Application::configure(basePath: dirname(__DIR__))
    ->withRouting(
        // web: __DIR__.'/../routes/web.php',
        commands: __DIR__.'/../routes/console.php',
        // health: '/up',
    )
```

### [[11.x] Add generics for Arr::first() by @phh](https://github.com/laravel/framework/pull/50514)

PHPStanによる型定義の強化。

### [Change default collation for MySQL by @driesvints](https://github.com/laravel/framework/pull/50555)

MySQLのcollationの設定を行なっているようですが何が行われているかまったくわからなかった...


### [[11.x] Fixes install:broadcasting command by @joedixon](https://github.com/laravel/framework/pull/50550)

Laravel10 => Laravel11 へアプリを移行する際にbroadcast機能でエラーが出ていたようですがそれを修正するようです(あまりわからなかった)。

### [[11.x] Fix crash when configuration directory is non-existing by @buismaarten](https://github.com/laravel/framework/pull/50537)

Laravel11になって、configを書かなくても良くなった。
しかし、空になったconfigのディレクトリを消すと、コンフィグを読む処理をしている箇所でバグったらしい。
コンフィグファイルがない場合は処理を続行しないようにしていた。