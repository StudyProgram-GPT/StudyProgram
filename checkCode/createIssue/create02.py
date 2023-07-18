import random
def createIssue02():
    absoluteInputFileName = "../issue/02/input_02_"
    for i in range(100):
        inputFileName = absoluteInputFileName + str(i).zfill(2) + ".txt"
        with open(inputFileName, "w") as file:
            numbers = [random.randint(-100, 100) for _ in range(4)]  # Generate first four numbers
            file.write(' '.join(map(str, numbers)))


def createAnswer02():
    absoluteInputFileName = "../issue/02/input_02_"
    with open("../answer/02/answer02.txt", "w") as out_file:
        for i in range(100):
            inputFileName = absoluteInputFileName + str(i).zfill(2) + ".txt"
            with open(inputFileName, "r") as in_file:
                for line in in_file:
                    numbers = list(map(int, line.split()))
                    result =  numbers[0] + numbers[1] - (numbers[2] * numbers[3])
                    out_file.write(str(result) + '\n')

createIssue02()
createAnswer02()