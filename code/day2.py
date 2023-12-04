from typing import Tuple
import re

cube_values_dict = {
    "green": 13,
    "red": 12,
    "blue": 14
}


def get_highest_values(ball_line: str) -> dict[str, int]:
    ball_list = ball_line.split(";")
    temp_ball_dict = {}

    for i in cube_values_dict:
        temp_ball_dict[i] = 0

    for i in ball_list:
        single_pull = i.split(",")
        for x in single_pull:
            value_and_ball = x.split()
            if int(value_and_ball[0]) > int(temp_ball_dict[value_and_ball[1]]):
                temp_ball_dict.update({value_and_ball[1]: value_and_ball[0]})

    return temp_ball_dict


def day_two(input_file: str) -> Tuple[int, int]:
    with open(input_file, "r") as f:
        line_list = f.read().splitlines()

    possible_games = 0
    highest_values_multiplied = 0
    game_dict = {}

    for i in line_list:
        game = re.findall(r'\d+', i[:i.index(":")])[0]
        highest_values = get_highest_values(i[i.index(":") + 1:])
        game_dict.update({game: highest_values})

    for i in game_dict:
        add_to_sum = True
        for color, value in cube_values_dict.items():
            if value < int(game_dict[i][color]):
                add_to_sum = False

        if add_to_sum:
            possible_games += int(i)

    for i in game_dict:
        hand_multiplied = 1
        for x in game_dict[i]:
            hand_multiplied = hand_multiplied * int(game_dict[i][x])
        highest_values_multiplied += hand_multiplied

    return possible_games, highest_values_multiplied

#(2164, 69929)