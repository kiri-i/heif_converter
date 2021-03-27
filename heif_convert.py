from PIL import Image
import pyheif
import pathlib


def conv(heic_path, save_dir):
    # ファイルの親ディレクトリを取得
    label_dir = heic_path.parent.name
    # 保存先のディレクトリとファイル名
    save_path = save_dir / label_dir / pathlib.Path(heic_path.name).with_suffix(".jpg")
    # フォルダ作成
    save_path.parent.mkdir(parents=True, exist_ok=True)

    # HEICファイルpyheifで読み込み
    heif_file = pyheif.read(heic_path)
    # 読み込んだファイルの中身をdata変数へ
    data = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
        )
    # JPEGで保存
    data.save(save_path, quality=95)
    print("保存：",save_path)


def main():
    # 変換対象のファイルがあるディレクトリ
    image_dir = pathlib.Path("./images/heic")
    # 保存先のディレクトリ
    save_dir = pathlib.Path("./images/jpg")

    # globでディレクトリ内のHEICファイルをリストで取得
    heic_paths = list(image_dir.glob('**/*.heic'))

    for heic_path in heic_paths:
        conv(heic_path, save_dir)
    print("完了")

if __name__ == "__main__":
    main()