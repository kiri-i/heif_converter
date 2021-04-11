# heif_converter

HEIF(.heicファイル)をまとめて変換できるPython CLIアプリ

ディレクトリ構造を保ったまま、複数ファイルを変換可能。  
Docker Desktop for Windowsで動作確認済

## 使い方
### Dockerイメージ作成

DockerfileからDockerイメージを作成
```shell
docker build -t heif_converter .
```

### Dockerコンテナ起動

コンテナを起動してheif_converterのHelpを表示

```shell
docker run -it --rm -v "$(pwd):/app" -w /app heif_converter python3 ./heif_converter.py --help
```

### inputとoutputディレクトリを指定して実行

<input_dir_path>と<output_dir_path>は任意のディレクトリのパスを指定する。

#### JPEGの場合（デフォルト）
```shell
docker run -it --rm -v "$(pwd):/app" -v "<input_dir_path>:/app/input" -v "<output_dir_path>:/app/output" -w /app heif_converter python3 /app/heif_converter.py
```

#### PNGの場合
```shell
docker run -it --rm -v "$(pwd):/app" -v "<input_dir_path>:/app/input" -v "<output_dir_path>:/app/output" -w /app heif_converter python3 /app/heif_converter.py --filetype="png"
```

## HEIF(.heic)ファイルとは
[Apple：HEIFファイル](https://support.apple.com/ja-jp/HT207022)

## 利用ライブラリ
[pyheif](https://github.com/carsales/pyheif)