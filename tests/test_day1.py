from unittest import TestCase
import os
import code

SEP = os.path.sep

FILE_DIC = {
    1: f"C:{SEP}GITHUB{SEP}AdventOfCode2023{SEP}files{SEP}input_day1.txt",
    2: f"C:{SEP}GITHUB{SEP}AdventOfCode2023{SEP}files{SEP}input_day2.txt"
}
class Test(TestCase):
    def test_day_one(self):
        result = code.day_one(FILE_DIC[1])
        self.assertEqual(result, 55093)

    def test_day_two(self):
        result1, result2 = code.day_two(FILE_DIC[2])
        self.assertEqual(result1, 2164)
        self.assertEqual(result2, 69929)
