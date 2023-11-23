# Advent of Code | Year 2022 | Day 2
# Author Robin Taylor

from typing import NamedTuple

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read()


class Solver:
    def __init__(self, input) -> None:
        self.my_score: int = 0
        self.b_score: int = 0
        self.scoring: dict = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
        a: list[str] = input.split("\n")
        self.hands: dict[str, str] = []
        for hand in a:
            x = hand.split()
            self.hands.append(x)

    def _evaluate_hand(self, theirs: int, mine: int) -> None:
        self.my_score += self.scoring[mine]

        # Draw
        if self.scoring[theirs] == self.scoring[mine]:
            self.my_score += 3
            return

        if (
            (theirs == "A" and mine == "Y")
            or (theirs == "B" and mine == "Z")
            or (theirs == "C" and mine == "X")
        ):
            self.my_score += 6
            return
        return

    def _evaluate_hand_strat_b(self, theirs: int, mine: int) -> None:
        # Win
        if mine == "Z":
            self.b_score += 6
            if theirs == "A":
                self.b_score += 2
            if theirs == "B":
                self.b_score += 3
            if theirs == "C":
                self.b_score += 1
            return

        # Draw
        if mine == "Y":
            self.b_score += 3
            self.b_score += self.scoring[theirs]
            return

        # Lose
        if mine == "X":
            if theirs == "A":
                self.b_score += 3
            if theirs == "B":
                self.b_score += 1
            if theirs == "C":
                self.b_score += 2
            return
        return

    def play(self):
        score = 0
        for hand in self.hands:
            their_play = hand[0]
            my_play = hand[1]
            self._evaluate_hand(theirs=their_play, mine=my_play)
            self._evaluate_hand_strat_b(theirs=their_play, mine=my_play)

    def run(self):
        self.play()
        print(self.my_score)
        print(self.b_score)


if __name__ == "__main__":
    s = Solver(input=input)
    s.run()
