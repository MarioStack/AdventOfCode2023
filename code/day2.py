import re
import math

game_dict = {}

cube_values_dict = {
    "green": 13,
    "red": 12,
    "blue": 14
}


def get_highest_values(game_num, ball_line):
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


def day_two(input_file):
    possible_games = 0
    highest_values_multiplied = 0

    line_list = open(input_file, "r").read().splitlines()
    for i in line_list:
        line_dict = {}
        game = re.findall(r'\d+', i[:i.index(":")])[0]

        highest_values = get_highest_values(game, i[i.index(":") + 1:])
        game_dict.update({game: highest_values})

    for i in game_dict:
        add_to_sum = True

        for x in cube_values_dict:
            if int(cube_values_dict[x]) >= int(game_dict[i][x]):
                continue
            else:
                add_to_sum = False

        if add_to_sum:
            possible_games += int(i)

    for i in game_dict:
        hand_multiplied = 1
        for x in game_dict[i]:
            hand_multiplied = hand_multiplied * int(game_dict[i][x])
        highest_values_multiplied += hand_multiplied

    return possible_games, highest_values_multiplied

