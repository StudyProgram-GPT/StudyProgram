import subprocess
import glob
import threading
import time
import signal
from checkCode import check01, check02

class TimeoutException(Exception):
    pass

def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException("タイムアウト")

    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)

def main(number, file):
    cmd = "gcc " + file
    #コンパイルが通るか確認
    try: 
        subprocess.run(cmd, shell = True, check=True)
    except subprocess.CalledProcessError as e:
        return -1, "コンパイルエラーです"
    except FileNotFoundError:
        return -1, "ファイルが存在しないです"    
    """
    (number, text):(答えがあってるか, 理由)
    (0, 'OK') 改行と問題の答えが両方ともあってる
    (1, '結果が異なります') 問題が違う(改行は記述しない)
    (1, "改行を入れて下さい") 問題はあってるが改行ができなてない
    (1, "Timeエラーが起きました")
    """
    #ここで呼び出された関数はこの階層にいるとして扱われる
    try:
        time_limit(5)  # 5秒を上限とする
        if number == 1: #HelloWorldの問題
            flag, text = check01.isuue01()
        elif number == 2:
            flag, text = check02.issue02() #足し算,引き算,掛け算
    except TimeoutException:
        flag = 1
        text = "Timeエラーが起きました"
    else:
        # アラームをキャンセル
        signal.alarm(0)

    return flag, text