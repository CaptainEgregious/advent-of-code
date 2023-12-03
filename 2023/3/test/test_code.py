import pytest
from code_3 import Solver


class TestSolver:
    def test_website_input(self):
        input = "467..114..\n...*......\n..35..633.\n......#...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598.."
        s = Solver(input_txt=input)
        assert s.run_one() == 4361

    def test_website_input_with_extra(self):
        input = "467..114..\n...*......\n..35..633.\n......#...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598..\n.755......\n......*755"
        s = Solver(input_txt=input)
        assert s.run_one() == 5116

    def test_gears(self):
        input = "467..114..\n...*......\n..35..633.\n......#...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598.."
        s = Solver(input_txt=input)
        assert s.run_two() == 467835
