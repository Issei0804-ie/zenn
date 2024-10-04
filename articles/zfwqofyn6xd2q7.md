---
title: "Laravel v11.0.5 まとめ"
emoji: "📘"
type: "tech"
topics:
  - "php"
  - "laravel"
  - "laravel11"
published: true 
---

30minで読めるだけ読んだので、全部のリリースはまとめきれてないこともあります。
リリースノートは[こちら](https://github.com/laravel/framework/releases/tag/v11.0.5)

- [11.x] Improves broadcasting install by @nunomaduro in https://github.com/laravel/framework/pull/50519
- [11.x] Improved exception message on 'ensure' method by @fgaroby in https://github.com/laravel/framework/pull/50517
- [11.x] Add hasValidRelativeSignatureWhileIgnoring macro by @br13an in https://github.com/laravel/framework/pull/50511
- [11.x] Prevents database redis options of being merged by @nunomaduro in https://github.com/laravel/framework/pull/50523

### [[11.x] Improves broadcasting install by @nunomaduro](https://github.com/laravel/framework/pull/50519)

本来、`uncommentChannelsRoutesFile`は`routes/channels.php`が存在しない時にのみ行われていたようだが、ファイルが存在していても実行できるようにしたっぽい。

uncommentChannelsRoutesFileメソッドは、`channels:`のコメントアウトをしているようです。

```php
# bootstrap/app.php
return Application::configure(basePath: dirname(__DIR__))
    ->withRouting(
        web: __DIR__.'/../routes/web.php',
        commands: __DIR__.'/../routes/console.php',
        channels: __DIR__.'/../routes/channels.php',  // ここがコメントアウトされていなかった場合、コメントアウトをしてくれるらしいです。
        health: '/up',
    )
    ->withMiddleware(function (Middleware $middleware) {
        //
    })
    ->withExceptions(function (Exceptions $exceptions) {
        //
    })->create();

```

ただ、内部のロジックを見てみると、そもそも`channles:` が存在しなかった場合は新しく行を追加して付け加えているので実は`uncomment`というよりも`set`の方がニュアンスとしては近いかもです。


### [[11.x] Improved exception message on 'ensure' method by @fgaroby](https://github.com/laravel/framework/pull/50517)

Collectionのensureメソッドで例外が発生する時のメッセージを改善したようです。

```
- Collection should only include [stdClass] items, but 'string' found.
+ Collection should only include [stdClass] items, but 'string' found at position 3.
```

ちなみにensureの役割は[こちら](https://laravel.com/docs/11.x/collections#method-ensure)。

> The ensure method may be used to verify that all elements of a collection are of a given type or list of types. Otherwise, an UnexpectedValueException will be thrown:

コレクションの各要素が引数に渡した型になっているか検証する。もし引数に渡した型以外が要素に存在した場合は、`UnexpectedValueException`を投げる。

試しに使ってみましょう。

```php
# 11.0.4(修正前)の場合
collect([1,2,'hoge'])->ensure('int');

   UnexpectedValueException  Collection should only include [int] items, but 'string' found.
```

```php
# 11.0.5(修正後)の場合
collect([1,2,'hoge'])->ensure('int');

   UnexpectedValueException  Collection should only include [int] items, but 'string' found at position 2.
```

こんな感じでどこの要素の型で検証が失敗したか教えてくれます。


### [Add hasValidRelativeSignatureWhileIgnoring macro by @br13an](https://github.com/laravel/framework/pull/50511)


Requestクラスのmacroとして、`hasValidRelativeSignatureWhileIgnoring`を追加しているようです。

```php
Request::macro('hasValidRelativeSignatureWhileIgnoring', function ($ignoreQuery = []) {
    return URL::hasValidSignature($this, $absolute = false, $ignoreQuery);
});
```

`URL::hasValidSignature`はこんな感じです。

```php
/**
 * Determine if the given request has a valid signature.
  *
  * @param  \Illuminate\Http\Request  $request
  * @param  bool  $absolute
  * @param  array  $ignoreQuery
  * @return bool
  */
public function hasValidSignature(Request $request, $absolute = true, array $ignoreQuery = [])
{
    return $this->hasCorrectSignature($request, $absolute, $ignoreQuery)
        && $this->signatureHasNotExpired($request);
}
```

### [[11.x] Prevents database redis options of being merged by @nunomaduro](https://github.com/laravel/framework/pull/50523)

Redisのクラスターを設定しようとした時にある条件を満たすと設定がマージされるようです(クラスタやったことないのでわからなかった..)。
