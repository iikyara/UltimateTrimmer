import os, sys, argparse, csv, re


# タイトル未指定の場合に代わりとなる感想の冒頭の文字数を指定
BOUTOU=5
# トリミング時間の拡張指定
EXPAND=[3,3]
# ファイル名に使用不可の文字を設定
BAT_PATTERN = r"\\|\/|:|\*|\?|\"|>|<|\||&|\(|\)|\[|\]|\{|\}|\^|=|;|!|'|\+|,|`|~|\r|\n|\r\n"

def main(args):
    print(args)
    csvnames = args.csv
    savedir = args.save

    for i in range(len(csvnames)):
        csvname = csvnames[i]
        trimVideoWithCSV(i, csvname, savedir)

def trimVideoWithCSV(video_number, csvname, savedir):
    print(f"- {csvname} 動画番号:{video_number}")

    # 入力チェック
    if not os.path.exists(csvname):
        print(f"  CSVファイルが見つかりませんでした。")
        return

    # トリミングデータの読み込み
    with open(csvname, encoding="utf-8") as f:
        reader = csv.reader(f)
        trim_infos = [row for row in reader]

    # 動画ファイルを見つける
    head = 0
    videoname = ""
    while True:
        if head >= len(trim_infos):
            print("  試合動画ファイルが見つかりませんでした。")
            return
        if len(trim_infos[head]) > 0 and os.path.exists(trim_infos[head][0]):
            videoname = trim_infos[head][0]
            break
        head += 1

    # 動画ファイルの拡張子を取得
    try:
        ext = os.path.splitext(videoname)[1]
    except:
        print(f"  拡張子が見つかりませんでした。")
        return

    # 保存ディレクトリの作成
    if not os.path.exists(savedir):
        os.mkdir(savedir)

    # トリミング
    while True:
        if head >= len(trim_infos):
            return
        print(f"  {head}行目：", end="")
        trim_info = trim_infos[head]
        filename = createFilename(video_number, trim_info, ext)
        if filename == None:
            print(f"フォーマットが間違っています。")
            head += 1
            continue
        isSave = trimVideo(trim_info, videoname, filename)
        if isSave:
            print(f"{filename}に保存されました。")
        else:
            print(f"{filename}動画のトリミング中にエラーが発生しました。")
        head += 1

# ファイル名を生成する
# 条件に合わない場合はNoneを返す
def createFilename(video_number, trim_info, ext):
    if len(trim_info) < 5:
        return None

    # 開始秒
    start = tryParse(trim_info[0])
    if not start:
        return None

    # 終了秒
    end = tryParse(trim_info[1])
    if not end:
        return None

    # 感想
    impression = trim_info[4]
    if impression == "":
        impression = "特に感想はありません"

    # 属性
    tags = trim_info[3].split()
    if len(tags) == 0:
        tags = ["NoTagged"]
    tagstr = "-".join(sorted(tags))

    # タイトル
    title = re.sub(BAT_PATTERN, "", trim_info[2])
    if title == "":
        title = impression[:BOUTOU]

    filename = f"{video_number}_{start}_{title}_{tagstr}{ext}"

    return re.sub(BAT_PATTERN, "", filename)

def tryParse(s):
    try:
        parsed = int(s, 10)
    except ValueError:
        return None
    return parsed

# 動画をトリミングする
# 成功：True，失敗：False
def trimVideo(trim_info, videoname, output):
    return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ビデオを切り抜くスクリプトです。CSVファイルを引数に指定してください。")
    parser.add_argument("csv", help="切り抜きのCSVファイルを指定してください。", nargs="*")
    parser.add_argument("--save", help="保存ディレクトリを指定してください。", default="trim/")
    args = parser.parse_args()
    main(args)
