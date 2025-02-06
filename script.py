import os
import sys
import pyhdi  # HDIファイルを扱うためのライブラリ

def extract_hdi(hdi_file):
    # HDIファイルを開く
    with pyhdi.HDIFile(hdi_file) as hdi:
        # HDI内のファイルをリストアップ
        files = hdi.list_files()
        
        os.makedirs("extracted_files", exist_ok=True)

        for file in files:
            # 各ファイルを読み込み
            content = hdi.read_file(file)
            # テキストファイルとして保存
            output_file = os.path.join("extracted_files", f"{file}.txt")
            with open(output_file, 'wb') as f:
                f.write(content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python your_script.py <hdi_file>")
        sys.exit(1)

    hdi_file = sys.argv[1]
    extract_hdi(hdi_file)
