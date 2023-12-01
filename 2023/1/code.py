# Advent of Code | Year 2023 | Day 1
# Author Robin Taylor
import re

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read()


class Solver:
    def __init__(self, input):
        self.input = input

    def run(self):
        total = 0
        for string in self.input.split("\n"):
            int_str = re.sub("\D", "", string)
            total += int(f"{int_str[0]}{int_str[-1:]}")
        print(total)

    def run_two(self):
        score = 0
        number_map = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }
        for string in self.input.split("\n"):
            regex = set(number_map.keys()).union(set(number_map.values()))
            p = re.findall(r"(?=(" + "|".join(regex) + r"))", string)
            if p[0] in list(number_map):
                int_str_1 = number_map[p[0]]
            else:
                int_str_1 = p[0]
            if p[-1] in list(number_map):
                int_str_2 = number_map[p[-1]]
            else:
                int_str_2 = (p[-1])
            score += int(f"{int_str_1}{int_str_2}")
        print(score)

if __name__ == "__main__":
    s = Solver(input=input)
    s.run()
    s.run_two()
