# Advent of Code | Year 2023 | Day 3
# Author Robin Taylor

import re


def load_file():
    with open((__file__.rstrip("code_3.py") + "input.txt"), "r") as input_file:
        input_txt = input_file.read()
    return input_txt


class Solver:
    def __init__(self, input_txt):
        self.input_split = input_txt.split("\n")
        self.special_chars = "!@#$%^&*()-+?_=,<>/"

    def get_chars_for_line(self, row_idx, start, length):
        return self.input_split[row_idx][start : start + length]

    def is_special_adjacant(self, row_idx, start, end) -> bool:
        surrounding_chars = ""
        # if line is not first line get above
        start_adjuster = 0
        if start == 0:
            start_adjuster += 1
        if row_idx != 0:
            surrounding_chars = surrounding_chars + self.get_chars_for_line(
                row_idx=row_idx - 1,
                start=start - 1 + start_adjuster,
                length=end - start + 2 - start_adjuster,
            )
        # if number is not beginning of line get first
        if start != 0:
            surrounding_chars = surrounding_chars + self.get_chars_for_line(
                row_idx=row_idx, start=start - 1, length=1
            )
        # if number is not end of line get last
        if end != len(self.input_split[row_idx]):
            surrounding_chars = surrounding_chars + self.get_chars_for_line(
                row_idx=row_idx, start=end, length=1
            )
        # if line is not last line get following chars
        if row_idx + 1 != len(self.input_split):
            surrounding_chars = surrounding_chars + self.get_chars_for_line(
                row_idx=row_idx + 1,
                start=start - 1 + start_adjuster,
                length=end - start + 2 - start_adjuster,
            )
        if any(not c not in self.special_chars for c in surrounding_chars):
            return True

        return False

    def run_one(self):
        running_total = 0
        row_idx = 0
        correct = []
        incorect = []
        for line in self.input_split:
            for x in re.finditer("\\d+", line):
                if self.is_special_adjacant(
                    row_idx=row_idx,
                    start=x.start(),
                    end=x.start() + len(x.group(0)),
                ):
                    running_total += int(x.group(0))
                    correct.append(int(x.group(0)))
                else:
                    incorect.append(x.group(0))
            row_idx += 1
        print(running_total)

        return running_total

    def search(self, line_idx, start) -> list:
        start_adjuster = 0
        if start > 2:
            start_adjuster += 1
        tmp_number_string = ""
        number_array = []
        position = 0
        for x in self.input_split[line_idx][max(start - 3, 0) : start + 4]:
            if x.isdigit():
                tmp_number_string = tmp_number_string + x
                if position + 1 == len(
                    self.input_split[line_idx][max(start - 3, 0) : start + 4]
                ):
                    number_array.append(tmp_number_string)
                    break
                position += 1
                continue
            # disregard numbers after * + 1 position
            # We've found ashort number that doesnt touch
            if position in [1, 2]:
                tmp_number_string = ""
            if tmp_number_string:
                number_array.append(tmp_number_string)
                tmp_number_string = ""
            if position >= 4:
                if tmp_number_string:
                    number_array.append(tmp_number_string)
                break
            # we have numbers, have not exited so much be 3 digits after half
            position += 1
        return number_array

    def gear_multiplication(self, line_idx, start, previous, next_line) -> int:
        # Above
        gear_list = self.search(previous, start)
        # current
        gear_list.extend(self.search(line_idx, start))
        # # After
        gear_list.extend(self.search(next_line, start))
        if len(gear_list) > 1:
            return int(gear_list[0]) * int(gear_list[1])
        return 0

    def run_two(self):
        gear_total = 0
        line_idx = 0
        previous = None
        next_line = 1
        for line in self.input_split:
            for x in re.finditer("\*", line):
                gear_total = gear_total + self.gear_multiplication(
                    line_idx=line_idx,
                    start=x.start(),
                    previous=previous,
                    next_line=next_line,
                )
            previous = line_idx
            line_idx += 1
            next_line += 1
            if next_line > len(self.input_split):
                next_line = None
        print(gear_total)
        return gear_total


if __name__ == "__main__":
    input_txt = load_file()
    s = Solver(input_txt=input_txt)
    s.run_one()
    s.run_two()
