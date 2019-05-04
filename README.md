## 大学生が休講情報を取ってくるdiscord botを作ってみた結果wwww

Campus Square を使っている大学生は全員使えると思います

## 最初にやるべきこと

- このファイルのダウンロード
右上の方にある`clone or download`を押してダウンロードし、解凍してください

- Firefoxのインストール
[こちら](https://www.mozilla.org/ja/firefox/new/) からどうぞ

- Discordのインストールとアカウント作成
[こちら](https://discordapp.com/) からどうぞ

- discord botの作成  
[この記事](https://qiita.com/PinappleHunter/items/af4ccdbb04727437477f) の**Botを書く**の**直前まで**をやってください  


- discord webhookの設定  
[この記事](https://support.discordapp.com/hc/ja/articles/228383668-%E3%82%BF%E3%82%A4%E3%83%88%E3%83%AB-Webhooks%E3%81%B8%E3%81%AE%E5%BA%8F%E7%AB%A0) の**WEBHOOKの作成**欄を見てトレースしてください  


- kyukou.pyに**ID**、**パスワード**、**WebhookのURL**を書き入れる

- kyukoubot.pyに**Botのトークン**を書き入れる

## Python3のインストール

- Linux
**なにもしなくてOK**

- MAC
[この記事](https://qiita.com/7110/items/1aa5968022373e99ae28) を見てインストール

- Windows
[この記事](https://qiita.com/taiponrock/items/f574dd2cddf8851fb02c) を見てインストール

## Power Shellの使い方(Windowsの方のみ)
[この記事](https://qiita.com/opengl-8080/items/bb0f5e4f1c7ce045cc57) を見てください


## pipでインストールするもの

- Beautifulsoup4
- selenium
- discord
- discord_webhook

```
$ pip3 install discord discord_webhook selenium beautifulsoup4
```

↑
これをTarminalまたはPower Shellにコピペ  

Linux/MACの方はTerminalで実行してください  
Windowsの方はPower Shellで実行してください

## 他にインストールすべきもの

- geckodriver

[この記事](https://qiita.com/hujuu/items/ef89c34fca955cc571ec) を見てインストールしてください  


## 実行方法

```ruby:terminal
cd ./Downloads/class-confirm   # windowsの方のみ

python3 kyukoubot.py
```

↑
これをTarminalまたはPower Shellにコピペ  

Linux/MACの方は、解凍したフォルダ内で右クリックを押して、`端末で開く`を押してから実行してください  
Windowsの方は上に習って実行してください

## お好みで
自分でサーバーを持っている方はサーバーにおいてbotを動かしっぱなしにするのもあり。サーバーをレンタルするのもあり。
**現在cloneしなくても使えるように頑張っています。こうご期待。**
~~卒業するまでにはなんとか完成させます~~

## テスト環境

OS : Ubuntu 19.04  
Language : Python 3.7  
Environment : Pycharm

## 使い方等質問

Twitter : @kuge_masa
Discord : masa#0662
