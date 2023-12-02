import code
import os

SEP = os.path.sep

FILE_DIC = {
    1: f"C:{SEP}GITHUB{SEP}AdventOfCode2023{SEP}files{SEP}input_day1.txt",
    2: f"C:{SEP}GITHUB{SEP}AdventOfCode2023{SEP}files{SEP}input_day2.txt"
}


def main():
    print(code.day_one(FILE_DIC[1]))
    print(code.day_two(FILE_DIC[2]))


if __name__ == '__main__':
    main()

