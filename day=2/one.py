import re


def determine_possibility_of_game(line: str) -> int:
    "Returns the ID of the game if possible, else 0"
    print(f"Checking possibility for '{line}'")
    split_line = re.match(r"^Game (?P<id>\d{1,3}): (?P<game>.*)$", line.strip())
    game_id = split_line["id"]

    max_cubes = {"red": 12, "green": 13, "blue": 14}
    "12 red cubes, 13 green cubes, and 14 blue cubes"
    for subset in split_line[2].split(';'):
        for cube_count_str in subset.split(", "):
            match = re.match(r"(?P<count>\d{1,2}) (?P<type>\w*)", cube_count_str.strip())

            # if match is None:
            #     print(f"line '{subset}' with cube_count_str '{cube_count_str}' gave no extractions")

            if int(match["count"]) > max_cubes[match["type"]]:
                return 0

    return int(game_id)


with open("input.txt") as file:
    game_list = file.readlines()

result = sum(determine_possibility_of_game(line) for line in game_list)
print(f"The sum of IDs of possible games is {result}")