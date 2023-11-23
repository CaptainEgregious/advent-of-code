# Advent of Code | Year 2022 | Day 1
# Author Robin Taylor

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read()


class Solver:
    def __init__(self, input) -> None:
        self.input = input
        pass

    def separate_input(self) -> list[int]:
        a = self.input.split("\n\n")
        result = [list(map(int, elf.split("\n"))) for elf in a]
        return result

    def biggest_elf(self, elves: list[int]) -> int:
        current_total = 0
        for elf in elves:
            print(elf)
            total = sum(elf)
            if total > current_total:
                current_total = total
        return current_total

    def run(self):
        elves = self.separate_input()
        highest_elf = self.biggest_elf(elves)
        print(f"biggest - {highest_elf}")


s = Solver(input=input)
s.run()

print("Part One : " + str(None))


print("Part Two : " + str(None))
