import subprocess

def issue01():
    cmd = "./a.out"
    result = subprocess.run(cmd, shell=True,capture_output=True,text=True).stdout #実行
    text = 'OK'
    newlineFlag = 0
    issueFlag = 0
    if result[-1] != "\n":
        newlineFlag = 1
        text = "改行を入れて下さい."
    
    result = result.rstrip("\n")
    if result != "Hello World!":
        issueFlag = 1
    
    if issueFlag == 1: #結果が異なる場合
        return 1, "結果が異なります."
    elif newlineFlag == 1: #改行をしていない場合
        return 1, text
    else: #クリア
        return 0, text
        
    