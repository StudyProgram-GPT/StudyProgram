import socket

def send_file(host, port, issue_number, file_path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port)) #接続
        s.sendall(issue_number.encode("UTF-8")) #問題番号を送る
        receive = s.recv(4096).decode() #受け取ったか確認
        if receive != "OK":
            return ["1", "問題番号が違います"]
        else:
            with open(file_path, 'rb') as f: 
                s.sendall(f.read()) #ファイルを送る
            s.sendall("\nfinish!!!".encode()) #最後の目印を送る
            receive = s.recv(4096).decode() #受け取ったか確認
            receive = receive.split()
            return receive
    


if __name__ == "__main__":
    host = 'localhost'
    port = 12345
    issue_number = "2"
    file_path = './testCodeFolder/02/error.c'  # The file to send
    send_file(host, port, issue_number, file_path)
