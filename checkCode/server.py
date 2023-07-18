import socket
import subprocess
import main
def start_server(host, port, output_file_path, python_script_path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()

        while True:
            conn, addr = s.accept() #受け入れる
            with conn:
                print('Connected by', addr)
                try:
                    number = conn.recv(1024).decode() #問題番号を受け取る
                    number = int(number) #数字に変換できないものはエラーが起き、NOを返す。
                except Exception:
                    conn.sendall("NO".encode())
                else:
                    conn.sendall("OK".encode())
                
                    try:
                        message = b""
                        with open(output_file_path, "wb") as f:
                            while True:
                                data = conn.recv(4096) #1024バイトずつ読み取る
                                message += data
                                if "finish!!!" in message.decode(): #終わりが来たら
                                    print("*"*100)
                                    message = message.decode()
                                    message = message.replace("finish!!!", "") 
                                    f.write(message.encode())  #encodeしてファイルに書き込み
                                    break

                    except Exception as e:
                        answer = "-1 ファイルのエラー"
                    else:
                        flag, text = main.main(number, output_file_path)
                        answer = str(flag) + " " + text
                    conn.sendall(answer.encode())

if __name__ == "__main__":
    host = 'localhost'
    port = 12345
    output_file_path = 'received_file.c'
    python_script_path = './main.py'  # The Python script to run
    start_server(host, port, output_file_path, python_script_path)
