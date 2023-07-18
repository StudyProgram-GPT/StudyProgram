from flask import Flask, render_template, request
import sendFile

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post', methods=['POST'])
def post():
    def save_as_c_file(text, filename):
        with open(filename, 'w') as file:
            file.write(text)
    code = request.form['code']

    # Cファイルとして保存する
    save_as_c_file(code, 'data.c')
    print(code)
    # flag, text = checkCodes.main(2, "data.c")
    receive = sendFile.send_file('localhost', 12345, '1', 'data.c')
    print(receive)
    return 'Code received.'


if __name__ == '__main__':
    app.run(debug=True)
