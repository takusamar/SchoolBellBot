# SchoolBellBot

Discord Bot

Discord のボイスチャンネルで決まった時刻にベルを鳴らしたい時に使います。

## 音声ファイル

お好きな mp3 ファイルを置いて下さい。

## ffmpeg, opus のセットアップ

実行環境に ffmpeg, opus をインストールしてください。

```
$ wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz
$ tar xvf ffmpeg-release-amd64-static.tar.xz
$ cd ffmpeg-4.3.1-amd64-static/
$ sudo cp ffmpeg /usr/local/bin

$ sudo yum install opus-devel
```

## Discord

Discord に自作 Bot を追加し TOKEN を取得します。

Bot を実行対象の Discord サーバーにこの Bot を追加します。

Bot を実行させるボイスチャンネルの ID をメモしてください。

## Bot の cron 設定

doSchoolBell.sh を鳴らしたい時刻に cron 設定します。
引数には、mp3 ファイル名、音声チャンネル ID を指定してください。

設定例

```
$ crontab -e
0,50 * * * 1-5 <path>/doSchoolBell.sh <mp3_file> <voice_channel_id> >/dev/null 2>&1
40 * * * 1-5 <path>/doSchoolBell.sh <mp3_file> <voice_channel_id> >/dev/null 2>&1
```
