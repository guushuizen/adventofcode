from collections import defaultdict
import math
import re


def determine_minimum_power_of_cubes(line: str) -> int:
    "Returns the ID of the game if possible, else 0"
    print(f"Checking possibility for '{line}'")
    split_line = re.match(r"^Game (?P<id>\d{1,3}): (?P<game>.*)$", line.strip())

    minimum_cubes = defaultdict(int)
    "12 red cubes, 13 green cubes, and 14 blue cubes"
    for subset in split_line[2].split(';'):
        for cube_count_str in subset.split(", "):
            match = re.match(r"(?P<count>\d{1,2}) (?P<type>\w*)", cube_count_str.strip())

            if (count := int(match["count"])) > minimum_cubes[match["type"]]:
                minimum_cubes[match["type"]] = count

    return math.prod(minimum_cubes.values())


with open("input.txt") as file:
    game_list = file.readlines()

result = sum(determine_minimum_power_of_cubes(line) for line in game_list)
print(f"The sum of cube powers of all games is {result}")