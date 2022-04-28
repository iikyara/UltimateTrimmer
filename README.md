# ULTIMATE TRIMMER
CSVファイルで指定した部分をトリミングするスクリプトです。

# 使い方
- 以下のコマンドを実行してください
```
$ python ultimate_trimmer.py csvfile1.csv csvfile2.csv ...
```
- 実行後、trimフォルダに切り抜き動画が保存されます。

# CSVファイルのフォーマット
|video|||||
|:--:|:--:|:--:|:--:|:--:|
|{ここに動画ファイル名}.mp4|||||
||||||
|開始秒|終了秒|タイトル|属性|感想|
|12|30|よくばり|free miss|よくできましたとしか言いようがない|
|5|20|どこまでも走る|run|すげえ良い感じ|

# その他
## 保存ディレクトリを変更したい場合
- --saveオプションでディレクトリを指定してください
  - 例：savedir/に保存
```
$ python ultimate_trimmer.py csvfile1.csv --save savedir/
```

## 動作環境
Windows＋python環境での動作を想定しています。
