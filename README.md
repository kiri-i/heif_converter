# heif_converter

HEIF(.heicファイル)をまとめて変換できるPython CLIアプリ

ディレクトリ構造を保ったまま、複数ファイルを変換可能。  
Dockerで動作確認済

## 使い方
### dockerイメージ作成
```shell
docker build -t heif_converter .
```
### dockerコンテナ起動
```shell
docker run -it --name="heif_converter" -v "$(pwd):/app" heif_converter
```
### アプリ起動
```shell
cd /app
python3 ./heif_converter --help
```

## HEIF(.heic)ファイルとは
[Apple：HEIFファイル](https://support.apple.com/ja-jp/HT207022)

## 利用ライブラリ
[pyheif](https://github.com/carsales/pyheif)