# Advent of Code | Year 2023 | Day 3
# Author Robin Taylor

import re


def load_file():
    with open((__file__.rstrip("code_4.py") + "input.txt"), "r") as input_file:
        input_txt = input_file.read()
    return input_txt


class Solver:
    def __init__(self, input_txt):
        self.input_split = input_txt.split("\n")
        self.special_chars = "!@#$%^&*()-+?_=,<>/"

    def get_line_total(line, winners, ticket):
        number_of_winners = set(winners).intersection(set(ticket))
        # print(f"number {number_of_winners}")
        if len(number_of_winners):
            return 2 ** (len(number_of_winners) - 1)
        return 0

    def run_one(self):
        score = 0
        for line in self.input_split:
            winners, tickets = line.split(":")[1].split("|")
            winners = re.findall("\d+", winners)
            tickets = re.findall("\d+", tickets)
            score += self.get_line_total(winners=winners, ticket=tickets)
        print(f"score - {score}")
        return score

    def get_line_with_copy(self, winners, tickets, line_idx):
        score = self.get_line_total(winners=winners, ticket=tickets)
        # print(f"Multiplying score {score} by {self.copy_list[line_idx] + 1}")
        score = score * (self.copy_list[line_idx] + 1)
        # score is known, if we know copies we can just next copies by current copies of ticket
        number_of_matches = len(set(winners).intersection(set(tickets)))
        for win in range(0, number_of_matches):
            if win > len(self.copy_list) - 1:
                break
            if line_idx + win + 1 > len(self.copy_list) - 1:
                break
            # print(f"adding {self.copy_list[line_idx] + 1} for {line_idx + win + 1}")
            self.copy_list[line_idx + win + 1] += self.copy_list[line_idx] + 1
        print(f"list is {self.copy_list}")
        print(f"final copy list {sum(self.copy_list) + len(self.copy_list)}")
        return score

    def run_two(self):
        self.copy_list = [0] * len(self.input_split)
        score = 0
        line_idx = 0
        for line in self.input_split:
            winners, tickets = line.split(":")[1].split("|")
            winners = re.findall("\d+", winners)
            tickets = re.findall("\d+", tickets)
            score += self.get_line_with_copy(
                winners=winners, tickets=tickets, line_idx=line_idx
            )
            line_idx += 1
        print(f"2 - {score}")
        return score


if __name__ == "__main__":
    input_txt = load_file()
    s = Solver(input_txt=input_txt)
    s.run_one()
    s.run_two()
