from PIL import Image
import pyheif
import pathlib
import fire
from tqdm import tqdm

def conv(heic_path, save_dir, filetype, quality):
    # 保存先のディレクトリとファイル名
    extension = "." + filetype
    save_path = save_dir / filetype / pathlib.Path(*heic_path.parts[1:]).with_suffix(extension)
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
    data.save(save_path, quality=quality)
    print("保存：",save_path)

def conv_files(input_dir="input", output_dir="output", filetype="jpg",quality=95):
    # 変換対象のファイルがあるディレクトリ
    image_dir = pathlib.Path(input_dir)
    # 保存先のディレクトリ
    save_dir = pathlib.Path(output_dir)
    # globでディレクトリ内のHEICファイルをリストで取得
    heic_paths = list(image_dir.glob('**/*.heic'))

    for heic_path in tqdm(heic_paths):
        conv(heic_path, save_dir, filetype, quality)
    print("完了")

if __name__ == "__main__":
    fire.Fire(conv_files)