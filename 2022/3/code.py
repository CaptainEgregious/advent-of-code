# Advent of Code | Year 2022 | Day 3
# Author Robin Taylor

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read()


class Solver:
    def __init__(self, input) -> None:
        self.input = input

    def process_items(self, items: list[str]) -> int:
        score = 0
        for item in items:
            score += ord(item.lower()) - 96
            if item.isupper():
                score += 26
        return score

    def process_pockets(self, first_pocket, second_pocket) -> str:
        return "".join(set(first_pocket).intersection(second_pocket))

    def puzzle_one(self):
        items = []
        for rucksack in self.input.split("\n"):
            first_pocket = rucksack[: len(rucksack) // 2]
            second_pocket = rucksack[len(rucksack) // 2 :]
            items.append(
                self.process_pockets(
                    first_pocket=first_pocket, second_pocket=second_pocket
                )
            )

        score = self.process_items(items=items)
        print(f"score 1 is {score}")

    def puzzle_two(self):
        rucksacks = self.input.split("\n")
        score = []
        while len(rucksacks) > 0:
            first = set(rucksacks.pop())
            second = set(rucksacks.pop())
            third = set(rucksacks.pop())
            overlap = first.intersection(second).intersection(third).pop()
            score.append(overlap)
        score = self.process_items(items=score)
        print(f"score 2 is {score}")

    def run(self):
        self.puzzle_one()
        self.puzzle_two()


if __name__ == "__main__":
    s = Solver(input=input)
    s.run()
