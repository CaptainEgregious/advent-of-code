import pytest
from code_7 import Solver

website_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


class TestSolver:
    def test_run_one(self):
        s = Solver(input=website_input)
        assert s.run_one() == 6440
