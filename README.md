# Heroku Python Mecab


## Buildpacks
* https://github.com/heroku/heroku-buildpack-multi


.buidpacks
```
https://github.com/sunny4381/heroku-buildpack-linuxbrew.git
```

.cellar
```
mecab
mecab-ipadic
```

** 環境変数
* LD_LIBRARY_PATH = '/app/.linuxbrew/lib'
* MECAB_PATH = '/app/.linuxbrew/lib/libmecab.so'


** PIPライブラリ
* natto-py


** オリジナル辞書を使う場合 Buildpacksにこれを追加
* https://github.com/weibeld/heroku-buildpack-run.git

デプロイ時にオリジナル辞書を生成するためのシェルを動かす
ルートディレクトリのbuildpack-run.shに下記を記述する
```
/app/.linuxbrew/Cellar/mecab/0.996/libexec/mecab/mecab-dict-index -d /app/.linuxbrew/lib/mecab/dic/ipadic -u original.dic -f utf-8 -t utf-8 dict.csv && touch .mecabrc && echo "dicdir = /app/.linuxbrew/lib/mecab/dic/ipadic" >> .mecabrc && echo "userdic = /app/original.dic" >> .mecabrc
```

で使える
