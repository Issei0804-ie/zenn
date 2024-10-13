---
title: "Laravel v11.0.8 まとめ"
emoji: "📘"
type: "tech"
topics:
  - "php"
  - "laravel"
  - "laravel11"
published: true
---

30minで読めるだけ読んだので、全部のリリースはまとめきれてないこともあります。
リリースノートは[こちら](https://github.com/laravel/framework/releases/tag/v11.0.8)

- [11.x] Change typehint for enum rule from string to class-string by @liamduckett in https://github.com/laravel/framework/pull/50603
- [11.x] Fixed enum and enum.backed stub paths after publish by @haroon-mahmood-4276 in https://github.com/laravel/framework/pull/50629
- [11.x] Fix(ScheduleListCommand): fix doc block for listEvent method by @saMahmoudzadeh in https://github.com/laravel/framework/pull/50638
- [11.x] Re: Fix issue with missing 'js/' directory in broadcasting installation command by @alnahian2003 in https://github.com/laravel/framework/pull/50657
- [11.x] Remove `$except` property from `ExcludesPaths` trait by @gdebrauwer in https://github.com/laravel/framework/pull/50644
- [11.x] Fix command alias registration and usage. by @timacdonald in https://github.com/laravel/framework/pull/50617
- [11.x] Fixed make:session-table Artisan command cannot be executed if a migration exists by @naopusyu in https://github.com/laravel/framework/pull/50615
- [11.x] Fix(src\illuminate\Queue): update doc block, Simplification of the code in RedisManager by @saMahmoudzadeh in https://github.com/laravel/framework/pull/50635
- [11.x] Add `--without-reverb` and `--without-node` arguments to `install:broadcasting` command by @duncanmcclean in https://github.com/laravel/framework/pull/50662
- [11.x] Fixed `trait` stub paths after publish by @haroon-mahmood-4276 in https://github.com/laravel/framework/pull/50678
- [11.x] Fixed `class` and `class.invokable` stub paths after publish by @haroon-mahmood-4276 in https://github.com/laravel/framework/pull/50676
- [10.x] Fix `Collection::concat()` return type by @axlon in https://github.com/laravel/framework/pull/50669
- [11.x] Fix adding multiple bootstrap providers with opcache by @jessarcher in https://github.com/laravel/framework/pull/50665
- [11.x] Allow `BackedEnum` and `UnitEnum` in `Rule::in` and `Rule::notIn` by @PerryvanderMeer in https://github.com/laravel/framework/pull/50680
- [10.x] Fix command alias registration and usage by @crynobone in https://github.com/laravel/framework/pull/50695



### [[11.x] Change typehint for enum rule from string to class-string by @liamduckett](https://github.com/laravel/framework/pull/50603)

PHPDocの修正。
`string`型で受け取っていた引数を`class-string`で受け取るようにしました。
`class-string`は渡された引数が正しいクラス名であるという意味の型らしいです。

以下[ドキュメント](https://phpstan.org/writing-php-code/phpdoc-types#class-string)の引用です。

> Both literal strings with valid class names ('stdClass') and class constants (\stdClass::class) are accepted as class-string arguments.

このようにクラス名を受け付けるようです。

### [[11.x] Fixed enum and enum.backed stub paths after publish by @haroon-mahmood-4276](https://github.com/laravel/framework/pull/50629)

Enumのstubを公開していた場合、そっちも優先的に参照するようにしたらしいです。


### [[11.x] Fix(ScheduleListCommand): fix doc block for listEvent method by @saMahmoudzadeh](https://github.com/laravel/framework/pull/50638)

PHPDocの修正。

### [[11.x] Re: Fix issue with missing 'js/' directory in broadcasting installation command by @alnahian2003](https://github.com/laravel/framework/pull/50657)

broadcast機能のインストールに失敗するバグの修正。

### [[11.x] Remove `$except` property from `ExcludesPaths` trait by @gdebrauwer](https://github.com/laravel/framework/pull/50644)

`ExcludesPaths`traitに`except`というプロパティが実装されていたが、`except`に値を設定できないので設計を変えたPR。
trait自身が宣言していないプロパティにアクセスしているのでちょっと使いにくい気がするので、
setter生やしちゃえばいいじゃん、という気持ちになった。

### [[11.x] Fix command alias registration and usage. by @timacdonald](https://github.com/laravel/framework/pull/50617)

下記のように設定したコマンドを`php artisan session:table`で実行できないバグの修正。

```php
#[AsCommand(name: 'make:session-table')]
class SessionTableCommand extends MigrationGeneratorCommand
{
    protected $name = 'make:session-table';

    protected $aliases = ['session:table'];
```

### [[11.x] Fixed make:session-table Artisan command cannot be executed if a migration exists by @naopusyu](https://github.com/laravel/framework/pull/50615)


### [[11.x] Fix(src\illuminate\Queue): update doc block, Simplification of the code in RedisManager by @saMahmoudzadeh](https://github.com/laravel/framework/pull/50635)

PHPDoc修正。

あとついでにコードを綺麗にしている。


### [[11.x] Add `--without-reverb` and `--without-node` arguments to `install:broadcasting` command by @duncanmcclean](https://github.com/laravel/framework/pull/50662)

broadcast機能インストール時、Reverbとecho.jsのインストールが行われるようになっていたが、`install:broadcasting --without-reverb --without-node`のように書くとインストールを行わないようにした。

### [[11.x] Fixed `trait` stub paths after publish by @haroon-mahmood-4276](https://github.com/laravel/framework/pull/50678)

`make:trait`を実行した時、stubを公開していた場合はそちらを使用するようにした。

### [[11.x] Fixed `class` and `class.invokable` stub paths after publish by @haroon-mahmood-4276](https://github.com/laravel/framework/pull/50676)

上と同じ。
`make:class`を実行した時、stubを公開していた場合はそちらを使用するようにした。

### [[10.x] Fix `Collection::concat()` return type by @axlon](https://github.com/laravel/framework/pull/50669)

PHPDocの修正。

### [[11.x] Fix adding multiple bootstrap providers with opcache by @jessarcher](https://github.com/laravel/framework/pull/50665)

OPCacheが有効な場合、`ServiceProvider::addProviderToBootstrapFile`が複数回呼ばれるらしい。
そもそもOPCacheについての説明は[こちら](https://www.php.net/manual/ja/intro.opcache.php)。
なぜOPCacheが原因になっているのかわからなかった...

### [[11.x] Allow `BackedEnum` and `UnitEnum` in `Rule::in` and `Rule::notIn` by @PerryvanderMeer](https://github.com/laravel/framework/pull/50680)

PHPDocの修正。

### [[10.x] Fix command alias registration and usage by @crynobone](https://github.com/laravel/framework/pull/50695)

[#50617](https://github.com/laravel/framework/pull/50617)の修正をv10に取り込むようです。
ちょっとよくわからなかった...