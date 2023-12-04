import pytest
from code_4 import Solver


class TestSolver:
    def test_website_input_1(self):
        input = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\nCard 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\nCard 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\nCard 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\nCard 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\nCard 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
        s = Solver(input_txt=input)
        assert s.run_one() == 13

    def test_website_input_2(self):
        input = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\nCard 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\nCard 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\nCard 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\nCard 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\nCard 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
        s = Solver(input_txt=input)
        assert s.run_two() == 28

    def test_this_string(self):
        input = "Card   1: 27 61 49 69 58 44  2 29 39 10 | 97 96 49 78 26 58 27 77 69  9 39 88 53 10  2 29 61 62 48 87 18 44 74 34 11"
        s = Solver(input_txt=input)
        assert s.run_one() == 512
