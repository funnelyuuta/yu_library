#!/usr/bin/env python3
#前回実行時移行の日付のリスト取得したい時用 

from pathlib import Path
from datetime import datetime, timedelta


BEFORE_RUNTIME = '.before_runtime.txt'
DATE_FORMAT = '%Y%m%d%H%M%S'


def timemain():
    time_list = []
    #現在時刻の取得
    runtime = datetime.now()
    before_time = get_before_runtime(BEFORE_RUNTIME, DATE_FORMAT)
    if before_time is None:
        print("初めての実行です")
    else:
        print(f"前回の実行時刻は {before_time} です")
    print(f"現在の実行時刻は {runtime} です")
    save_before_runtime(runtime, BEFORE_RUNTIME, DATE_FORMAT)
    start = before_time
    end = runtime
    day = end - start
    #.days は経過日数の表示
    for i in range(day.days):
        #startからi日足した日数をtime_listへ追加していく
        curr = start + timedelta(days=i)
        #指定した形式の文字列へ変換
        a = curr.strftime('%Y%m%d')
        print(a)
        time_list.append(a)
    return time_list


def get_before_runtime(before_file, date_format):
    before_path = Path(before_file)
    before_time = None
    #もしファイルが存在したら、そのファイルから一行読み込み返し、ないならNoneを返す
    if before_path.exists():
        try:
            with before_path.open() as fd:
                #そのファイルから一行読み込みSTR型として保存
                before_str = fd.readline()
                #改行コードを除去
                before_str = before_str.strip()
                #文字列から指定した形式の時間型に変換
                before_time = datetime.strptime(before_str, date_format)
        except Exception as error:
            print(error)
    return before_time


def save_before_runtime(runtime, before_file, date_format):
    before_path = Path(before_file)
    try:
        with before_path.open('w') as fd:
            before_str = datetime.strftime(runtime, date_format)
            fd.write(before_str)
    except Exception as error:
        print(error)
