---
title: "Laravel v11.1.0 まとめ"
emoji: "📘"
type: "tech"
topics:
  - "php"
  - "laravel"
  - "laravel11"
published: false
---

30minで読めるだけ読んだので、全部のリリースはまとめきれてないこともあります。
リリースノートは[こちら](https://github.com/laravel/framework/releases/tag/v11.1.0)

- [11.x] MySQL transaction isolation level fix by @mwikberg-virta in https://github.com/laravel/framework/pull/50689
- [11.x] Add ListManagementOptions in SES mail transport by @arifszn in https://github.com/laravel/framework/pull/50660
- [11.x] Accept non-backed enum in database queries by @gbalduzzi in https://github.com/laravel/framework/pull/50674
- [11.x] Add `Conditionable` trait to `Context` by @michaelnabil230 in https://github.com/laravel/framework/pull/50707
- [11.x] Adds `@throws` section to the Context's doc blocks by @rnambaale in https://github.com/laravel/framework/pull/50715
- [11.x] Test modifying nullable columns by @hafezdivandari in https://github.com/laravel/framework/pull/50708
- [11.x] Introduce HASH_VERIFY env var by @valorin in https://github.com/laravel/framework/pull/50718
- [11.x] Apply default timezone when casting unix timestamps by @daniser in https://github.com/laravel/framework/pull/50751
- [11.x] Fixes `ApplicationBuilder::withCommandRouting()` usage by @crynobone in https://github.com/laravel/framework/pull/50742
- [11.x] Register console commands, paths and routes after the app is booted by @plumthedev in https://github.com/laravel/framework/pull/50738
- [11.x] Enhance malformed request handling by @jnoordsij in https://github.com/laravel/framework/pull/50735
- [11.x] Adds `withSchedule` to `bootstrap/app.php` file by @nunomaduro in https://github.com/laravel/framework/pull/50755
- [11.x] Fix dock block for create method in `InvalidArgumentException.php` by @saMahmoudzadeh in https://github.com/laravel/framework/pull/50762
- [11.x] signature typo by @abrahamgreyson in https://github.com/laravel/framework/pull/50766
- [11.x] Simplify `ApplicationBuilder::withSchedule()` by @crynobone in https://github.com/laravel/framework/pull/50765

### [[11.x] MySQL transaction isolation level fix by @mwikberg-virta](https://github.com/laravel/framework/pull/50689)

MySQL使用時、トランザクション分離レベルを指定するとエラーを投げて処理が落ちるバグの修正。
どうやらトランザクション分離レベルを指定するシンタックスが間違っていたようです。

###[[11.x] Add ListManagementOptions in SES mail transportby @arifszn](https://github.com/laravel/framework/pull/50660)

AWSのSESには送信メールに登録解除リンクを自動で追加する機能があるらしいです。
公式のドキュメントはこれですね。
https://docs.aws.amazon.com/ja_jp/ses/latest/dg/sending-email-list-management.html#configuring-list-management-list-contacts
その機能をLaravel側から使用できるようにするPRです。

- [[11.x] Accept non-backed enum in database queries by @gbalduzzi](https://github.com/laravel/framework/pull/50674)


下記のUserモデルに対して、QueryBuilderを介してスカラー値を持たないEnumを使用するとバグるらしい。

```php
enum Status 
{
    case Active;
    case Archive;
}

class User extends Model 
{
  protected $casts = [
    'status' => Status::class,
  ];
}
```

たとえば、このようにQueryBuilderを使用しない場合は上手く保存できる。

```php 
$user = new User();
$user->status = Status::Active; // Stored as 'Active' in the database
$user->save();
```


ただ、このようにQueryBuilderを使用するとエラーが出るらしい。
```php
User::where('status', Status::Active)->get(); // ❌ ERROR: Object of class Status could not be converted to string

User::update([ 'status' => Status::Archive]); // ❌ ERROR: Object of class Status could not be converted to string
```

解決方法として、QueryBuilder内でスカラー値を持たないEnumを使用するときはそのEnumの名前を使用するようにしたようです。

- [[11.x] Add `Conditionable` trait to `Context` by @michaelnabil230](https://github.com/laravel/framework/pull/50707)

`Context`に`src/Illuminate/Conditionable/Traits/Conditionable`をtraitとして追加するようです。

`Conditionable`を使用すると、whenとunlessが使用できるようになります。

```php
 # Conditionableについて
 /**
     * Apply the callback if the given "value" is (or resolves to) truthy.
     */
    public function when($value = null, ?callable $callback = null, ?callable $default = null)
 /**
     * Apply the callback if the given "value" is (or resolves to) falsy.
     */
    public function unless($value = null, ?callable $callback = null, ?callable $default = null)
```

使用例

```php
  Context::when(
    auth()->user()->isAdmin(),
    fn ($context) => $context->add('user', ['key' => 'other data', ...auth()->user()]),
    fn ($context) => $context->add('user', auth()->user()),
);
```

- [11.x] Adds `@throws` section to the Context's doc blocks by @rnambaale in https://github.com/laravel/framework/pull/50715
- [11.x] Test modifying nullable columns by @hafezdivandari in https://github.com/laravel/framework/pull/50708
- [11.x] Introduce HASH_VERIFY env var by @valorin in https://github.com/laravel/framework/pull/50718
- [11.x] Apply default timezone when casting unix timestamps by @daniser in https://github.com/laravel/framework/pull/50751
- [11.x] Fixes `ApplicationBuilder::withCommandRouting()` usage by @crynobone in https://github.com/laravel/framework/pull/50742
- [11.x] Register console commands, paths and routes after the app is booted by @plumthedev in https://github.com/laravel/framework/pull/50738
- [11.x] Enhance malformed request handling by @jnoordsij in https://github.com/laravel/framework/pull/50735
- [11.x] Adds `withSchedule` to `bootstrap/app.php` file by @nunomaduro in https://github.com/laravel/framework/pull/50755
- [11.x] Fix dock block for create method in `InvalidArgumentException.php` by @saMahmoudzadeh in https://github.com/laravel/framework/pull/50762
- [11.x] signature typo by @abrahamgreyson in https://github.com/laravel/framework/pull/50766
- [11.x] Simplify `ApplicationBuilder::withSchedule()` by @crynobone in https://github.com/laravel/framework/pull/50765