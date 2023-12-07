# Advent of Code | Year 2023 | Day 7
# Author Robin Taylor

with open((__file__.rstrip("code_7.py") + "input.txt"), "r") as input_file:
    input = input_file.read()


class Solver:
    def __init__(self, input):
        self.input = input
        self.hand_rankings = {
            "5OAC": 7,
            "4OAC": 6,
            "FH": 5,
            "3OAC": 4,
            "TP": 3,
            "OP": 1,
            "HK": 1,
        }

    def process_single_hand(self, hand):
        result = [[x] * hand.count(x) for x in set([*hand])]
        has_pair = False
        has_three_kind = False
        top_score = 0
        for group in result:
            if len(group) > top_score:
                top_score = len(group)
            if len(group) == 2:
                has_pair == True
            if len(group) == 3:
                has_three_kind == True
            if has_pair and has_three_kind:
                # Cant have 5 or 4 if we have fh
                top_score = 5
        return top_score

    def run_one(self):
        total_score = 0
        for hand in self.input.split("\n"):
            score = self.process_single_hand(hand.split(" ")[0])

        return

    def run_two(self):
        return


if __name__ == "__main__":
    s = Solver(input=input)
    s.run_one()
    s.run_two()
