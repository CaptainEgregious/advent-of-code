# Advent of Code | Year 2022 | Day 1
# Author Robin Taylor

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read()


class Solver:
    def __init__(self, input) -> None:
        self.input = input
        self.first: int = 0
        self.second: int = 0
        self.third: int = 0
        pass

    def separate_input(self) -> list[int]:
        a = self.input.split("\n\n")
        result = [list(map(int, elf.split("\n"))) for elf in a]
        return result

    def process_total(self, inspection: int):
        if inspection > self.first:
            self.first, inspection = inspection, self.first
        if inspection > self.second:
            self.second, inspection = inspection, self.second
        if inspection > self.third:
            self.third, inspection = inspection, self.third
        return

    def biggest_elf(self, elves: list[int]) -> None:
        current_total = 0
        for elf in elves:
            total = sum(elf)
            self.process_total(inspection=total)
        return current_total

    def run(self):
        elves = self.separate_input()
        self.biggest_elf(elves)
        print(f"biggest - {self.first}")
        print(f"combined = {sum([self.first,self.second, self.third])}")


s = Solver(input=input)
s.run()
