import unittest
import sendFile

class TestFunc(unittest.TestCase): #テストのためのクラス
    global host, port
    host = 'localhost'
    port = 12345
    def test_issue02_correct(self): #正解コード
        issue_number = "2"
        file_path = "./testCodeFolder/02/correct.c"
        expected = ["0", "OK"]
        actual = sendFile.send_file(host, port, issue_number, file_path)
        self.assertAlmostEqual(expected, actual)

    def test_issue02_newline(self): #改行していないコード
        issue_number = "2"
        file_path = "./testCodeFolder/02/newline.c"
        expected = ["1", "改行を入れて下さい"]
        actual = sendFile.send_file(host, port, issue_number, file_path)
        self.assertAlmostEqual(expected, actual)

    def test_issue02_mistake(self): #答えが間違いのコード
        issue_number = "2"
        file_path = "./testCodeFolder/02/mistake.c"
        expected = ["1", "結果が異なります"]
        actual = sendFile.send_file(host, port, issue_number, file_path)
        self.assertAlmostEqual(expected, actual)

    def test_issue02_error(self): #コンパイルエラーのコード
        issue_number = "2"
        file_path = "./testCodeFolder/02/error.c"
        expected = ["-1", "コンパイルエラーです"]
        actual = sendFile.send_file(host, port, issue_number, file_path)
        self.assertAlmostEqual(expected, actual)
    
    def test_issue02_timeError(self): #タイムエラーのコード
        issue_number = "2"
        file_path = "./testCodeFolder/02/timeError.c"
        expected = ["1", "Timeエラーが起きました"]
        actual = sendFile.send_file(host, port, issue_number, file_path)
        self.assertAlmostEqual(expected, actual)

    def test_issue02_notScanf(self): #scanfがない場合のコード
        issue_number = "2"
        file_path = "./testCodeFolder/02/notScanf.c"
        expected = ["1", "結果が異なります"]
        actual = sendFile.send_file(host, port, issue_number, file_path)
        self.assertAlmostEqual(expected, actual)

    def test_issue_fewScanf(self): #scanfが少ない場合のコード
        issue_number = "2"
        file_path = "./testCodeFolder/02/fewScanf.c"
        expected = ["1", "結果が異なります"]
        actual = sendFile.send_file(host, port, issue_number, file_path)
        self.assertAlmostEqual(expected, actual)
    
    def test_issue_manyScanf(self): #scanfが多い場合のコード
        issue_number = "2"
        file_path = "./testCodeFolder/02/manyScanf.c"
        expected = ["0", "OK"]
        actual = sendFile.send_file(host, port, issue_number, file_path)
        self.assertAlmostEqual(expected, actual)
    
    def test_issue_surplusScanf(self): #scanfに余分な文字
        issue_number = "2"
        file_path = "./testCodeFolder/02/surplusScanf.c"
        expected = ["1", "結果が異なります"]
        actual = sendFile.send_file(host, port, issue_number, file_path)
        self.assertAlmostEqual(expected, actual)
    
    def test_issue_empty(self): #ファイルが白紙の場合のコード
        issue_number = "2"
        file_path = "./testCodeFolder/02/empty.c"
        expected = ["-1", "コンパイルエラーです"]
        actual = sendFile.send_file(host, port, issue_number, file_path)
        self.assertAlmostEqual(expected, actual)

    def test_issue_manyText(self): #長いコード
        issue_number = "2"
        file_path = "./testCodeFolder/02/manyText.c"
        expected = ["-1", "ファイルのエラー"]
        actual = sendFile.send_file(host, port, issue_number, file_path)
        self.assertAlmostEqual(expected, actual)

    def test_issue_surplus(self): #回答に余分がはいってるコード
        issue_number = "2"
        file_path = "./testCodeFolder/02/surplus.c"
        expected = ["1", "結果が異なります"]
        actual = sendFile.send_file(host, port, issue_number, file_path)
        self.assertAlmostEqual(expected, actual)
        
    def test_issue_frontNewLine(self): #回答の前に改行を入れるコード
        issue_number = "2"
        file_path = "./testCodeFolder/02/frontNewline.c"
        expected = ["1", "結果が異なります"]
        actual = sendFile.send_file(host, port, issue_number, file_path)
        self.assertAlmostEqual(expected, actual)
    
    def test_issue_mistakeIssueNumber(self): #問題番号が数字以外の時
        issue_number = "a"
        file_path = "./testCodeFolder/02/frontNewline.c"
        expected = ["1", "問題番号が違います"]
        actual = sendFile.send_file(host, port, issue_number, file_path)

        self.assertAlmostEqual(expected, actual)
    
if __name__ == "__main__":
    unittest.main()
