# Advent of Code | Year 2023 | Day 2
# Author Robin Taylor

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read()


class Solver:
    def __init__(self, input):
        self.input = input
        self.games = input.split
        self.totals = {"green": 13, "red": 12, "blue": 14}

    def is_hand_valid(self, hand) -> bool:
        selections = hand.split(", ")
        for selection in selections:
            colour = selection.strip().split(" ")[1]
            volume = selection.strip().split(" ")[0]
            if self.totals[colour] < int(volume):
                return False
        return True

    def is_game_valid(self, game) -> bool:
        for hand in game.split(";"):
            if not self.is_hand_valid(hand):
                return False
        return True

    def process_game_totals(self, games):
        total = 0
        for game in games:
            print(f"game - {game}")
            total += int(game.split(" ")[1])
        return total

    def run_one(self):
        games = []
        for game in self.input.split("\n"):
            name = game.split(":")[0]
            if self.is_game_valid(game.split(":")[1]):
                games.append(name)
        total = self.process_game_totals(games)
        print(f"1 = {total}")

    def product_list(self, input_list) -> int:
        result = 1
        for i in input_list:
            result = result * i
        return result

    def minimum_counter_score(self, game) -> int:
        minimum_score = {
            "blue": 0,
            "red": 0,
            "green": 0,
        }
        for selection in game.split(";"):
            for choice in selection.split(", "):
                colour = choice.strip().split(" ")[1]
                volume = choice.strip().split(" ")[0]
                if int(volume) > minimum_score[colour]:
                    minimum_score[colour] = int(volume)
        return self.product_list(minimum_score.values())

    def run_two(self):
        total = 0
        for game in self.input.split("\n"):
            total += self.minimum_counter_score(game.split(":")[1])
        print(f"2 - {total}")
        return


if __name__ == "__main__":
    s = Solver(input=input)
    s.run_one()
    s.run_two()
