import re

DIGITS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def maybe_convert_to_actual_number(extracted: str) -> str:
    return str(DIGITS[extracted]) if len(extracted) > 1 else extracted


def read_first_and_last_value(line: str) -> int:
    matches = re.findall(pattern=r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', string=line.strip())
    return int(maybe_convert_to_actual_number(matches[0]) + maybe_convert_to_actual_number(matches[-1]))


if __name__ == "__main__":
    with open("./input.txt") as f:
        content = f.readlines()

    value = sum(read_first_and_last_value(line) for line in content)
    print(f"The calibration value is: {value}")
