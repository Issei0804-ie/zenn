---
title: "Laravel v11.0.7 まとめ"
emoji: "📘"
type: "tech"
topics:
  - "php"
  - "laravel"
  - "laravel11"
published: true
---

30minで読めるだけ読んだので、全部のリリースはまとめきれてないこともあります。
リリースノートは[こちら](https://github.com/laravel/framework/releases/tag/v11.0.7)

- [11.x] Re-add translations for ValidationException by @driesvints in https://github.com/laravel/framework/pull/50546
- [11.x] Removes unused Dumpable trait by @OussamaMater in https://github.com/laravel/framework/pull/50559
- [11.x] Fix withRouting docblock type by @santigarcor in https://github.com/laravel/framework/pull/50563
- [11.x] Fix docblock in FakeInvokedProcess.php by @saMahmoudzadeh in https://github.com/laravel/framework/pull/50568
- [11.x] fix: Add missing InvalidArgumentException import to Database/Schema/SqlServerBuilder by @ayutaya in https://github.com/laravel/framework/pull/50573
- [11.x] Improved translation for displaying the count of errors in the validation message by @andrey-helldar in https://github.com/laravel/framework/pull/50560
- [11.x] Fix retry_after to be an integer by @driesvints in https://github.com/laravel/framework/pull/50580
- [11.x] Use available `getPath()` instead of using `app_path()` to detect if base controller exists by @crynobone in https://github.com/laravel/framework/pull/50583
- [11.x] Fix doc block: `@return static` has been modified to `@return void` by @saMahmoudzadeh in https://github.com/laravel/framework/pull/50592
- accept attributes for channels by @taylorotwell in https://github.com/laravel/framework/commit/398f49485e305756409b52af64837c784fd30de9


### [[11.x] Re-add translations for ValidationException by @driesvints](https://github.com/laravel/framework/pull/50546)

- Validationが失敗した時に作成されるエラーのまとめが翻訳されないバグの修正
- Laravel11になってからのエラーのようです。

Laravel10の場合

```php
[{
    "message": "Le champ foo est obligatoire. (et 3 erreurs en plus)",
    // ...
}]
```

Laravel11の場合
```php
[{
    "message": "Le champ foo est obligatoire. (and 3 more errors)",
    // ...
}].
```

確かにLaravel11になってから丸括弧の中が訳されてない。


### [[11.x] Removes unused Dumpable trait by @OussamaMater](https://github.com/laravel/framework/pull/50559)

過去に`Query/Builder`に`Dumpable`というtraitが追加されたため実装されていた`dd`は削除された。
しかし、`Query/Builder`を確認したところ`Dumpable`は追加されたままで`dd`もメソッドとして存在していた。
そのため、`Dumpable`の方を削除するというPR。

### [[11.x] Fix withRouting docblock type by @santigarcor](https://github.com/laravel/framework/pull/50563)

実際に定義されているメソッドの引数の型とPHPDocの型が一致しなかったようで、その修正をしている。


### [[11.x] Fix docblock in FakeInvokedProcess.php by @saMahmoudzadeh](https://github.com/laravel/framework/pull/50568)

メソッドの引数の名前とPHPDocに記載されている引数の名前が一致しなかったようで、その修正をしている。

### [[11.x] fix: Add missing InvalidArgumentException import to Database/Schema/SqlServerBuilder by @ayutaya](https://github.com/laravel/framework/pull/50573)

`SqlServerBuilder`の中で`InvalidArgumentException`が投げられているが、このExceptionのクラスをインポートしていないバグの修正。

### [[11.x] Improved translation for displaying the count of errors in the validation message by @andrey-helldar](https://github.com/laravel/framework/pull/50560)

ロシア語、ウクライナ語などの言語では、複数形の中にさらに形が変わるものが存在するらしい(なんと)。

| Count | English | Russian | Ukrainian |
|----|------|----------|--------------|
| 1  | error | ошибка | помилка |
| 2  | errors | ошибки | помилки |
| 5  | errors | ошибок | помилок |


現在のバリデーションエラーの概要を表示するメッセージでは、複数形が正しく書かれていないようで、その修正を行うPR。

### [[11.x] Fix retry_after to be an integer by @driesvints](https://github.com/laravel/framework/pull/50580)

queueの設定で`retry_after`という設定が存在しており`config/queue.php`にはこんな感じで書かれている。

```php
'retry_after' => env('DB_QUEUE_RETRY_AFTER', 90),
```

これをLaravelで読み取ると、文字列の90として読み取ってしまうらしく、バグったらしい。
このPRでは単純にintにキャストしている

```php
# 編集後
'retry_after' => (int) env('DB_QUEUE_RETRY_AFTER', 90),
```


### [[11.x] Use available `getPath()` instead of using `app_path()` to detect if base controller exists by @crynobone](https://github.com/laravel/framework/pull/50583)

基底のコントローラーファイルの検索方法を`app_path`から`$this->getPath`に変更していたが変更する理由がわからなかった...

### [[11.x] Fix doc block: `@return static` has been modified to `@return void` by @saMahmoudzadeh](https://github.com/laravel/framework/pull/50592)

PHPDocの修正。

### [accept attributes for channels by @taylorotwell](https://github.com/laravel/framework/commit/398f49485e305756409b52af64837c784fd30de9)

`withBroadcasting`を設定する時に、`attributes`を引数として渡せるようにしている。

軽く追ってみた感じだと、middlewareなどの設定が行えるようです。

```php
/**
 * Register the routes for handling broadcast channel authentication and sockets.
  *
  * @param  array|null  $attributes
  * @return void
  */
public function routes(?array $attributes = null)
{
    if ($this->app instanceof CachesRoutes && $this->app->routesAreCached()) {
        return;
    }

    $attributes = $attributes ?: ['middleware' => ['web']];

    $this->app['router']->group($attributes, function ($router) {
        $router->match(
            ['get', 'post'], '/broadcasting/auth',
            '\\'.BroadcastController::class.'@authenticate'
        )->withoutMiddleware([\Illuminate\Foundation\Http\Middleware\VerifyCsrfToken::class]);
    });
}
```