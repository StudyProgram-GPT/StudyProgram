import subprocess
def issue02():
    f = open('./answer/02/answer02.txt', 'r', encoding='UTF-8')
    datalist = f.readlines()
    for i, data in enumerate(datalist):
        data = data.rstrip("\n")
        cmd = "./a.out < " + "./issue/02/input_02_" + str(i).zfill(2) + ".txt"
        result = subprocess.run(cmd, shell=True,capture_output=True,text=True).stdout #実行
        newlineFlag = 0
        issueFlag = 0
        if result[-1] != "\n":
            newlineFlag = 1

        result = result.rstrip("\n")
        
        if result != str(data):
            issueFlag = 1
        if issueFlag == 1: #結果が異なる場合
            return 1, "結果が異なります"
        elif newlineFlag == 1: #改行が入ってない場合
            return 1, "改行を入れて下さい"
    f.close()                        

    return 0, "OK"
