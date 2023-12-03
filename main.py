import code
import os

SEP = os.path.sep
ABSOLUTE_PATH = os.path.dirname(__file__)

FILE_DIC = {
    1: f"{ABSOLUTE_PATH}{SEP}files{SEP}input_day1.txt",
    2: f"{ABSOLUTE_PATH}{SEP}files{SEP}input_day2.txt",
    3: f"{ABSOLUTE_PATH}{SEP}files{SEP}input_day3.txt"
}


def main():
    print(code.day_one(FILE_DIC[1]))
    print(code.day_two(FILE_DIC[2]))
    print(code.day_three(FILE_DIC[3]))


if __name__ == '__main__':
    main()

