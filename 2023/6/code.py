# Advent of Code | Year 2023 | Day 6
# Author Robin Taylor

import re

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read()


class Solver:
    def __init__(self, input):
        self.input = input

    def prod_list(self, list):
        idx = 1
        for i in list:
            idx = idx * i
        return idx

    def run_one(self):
        races = self.input[0]
        time = list(
            map(int, re.findall("\d+", self.input.split("\n")[0].split(":")[1]))
        )
        distance = list(
            map(int, re.findall("\d+", self.input.split("\n")[1].split(":")[1]))
        )
        power = 0
        wins = []
        for race in time:
            was_beaten = 0
            for seconds_held in range(0, race):
                if distance[time.index(race)] < (race - seconds_held) * seconds_held:
                    was_beaten += 1
            wins.append(was_beaten)
        print(f"1 - {self.prod_list(wins)}")
        return self.prod_list(wins)

    def run_two(self):
        races = self.input[0]
        time = list(
            map(
                int,
                re.findall(
                    "\d+", self.input.split("\n")[0].split(":")[1].replace(" ", "")
                ),
            )
        )
        distance = list(
            map(
                int,
                re.findall(
                    "\d+", self.input.split("\n")[1].split(":")[1].replace(" ", "")
                ),
            )
        )
        power = 0
        wins = []
        for race in time:
            was_beaten = 0
            for seconds_held in range(0, race):
                if distance[time.index(race)] < (race - seconds_held) * seconds_held:
                    was_beaten += 1
            wins.append(was_beaten)
        print(f"2 - {self.prod_list(wins)}")
        return self.prod_list(wins)


if __name__ == "__main__":
    s = Solver(input=input)
    s.run_one()
    s.run_two()
