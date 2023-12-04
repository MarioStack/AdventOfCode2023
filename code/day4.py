import re


def day_four(input_file: str) -> int:
    with open(input_file, "r") as file:
        input_data = file.read().splitlines()

    winning_numbers_dict = {}
    hand_numbers_dict = {}

    for line_number, line in enumerate(input_data):
        winning_numbers = line[line.index(":") + 1:line.index("|")]
        hand_numbers = line[line.index("|") + 2:]

        winning_numbers_dict[line_number + 1] = re.findall(r'\d+', winning_numbers)
        hand_numbers_dict[line_number + 1] = re.findall(r'\d+', hand_numbers)

    total_count = 0

    for key in winning_numbers_dict:
        temp_score = 0
        counter = 1

        for wining_number in winning_numbers_dict[key]:
            if wining_number in hand_numbers_dict[key]:
                if temp_score == 0 and counter <= 3:
                    temp_score += 1
                    counter += 1
                else:
                    temp_score *= 2
                    counter += 1
        total_count += temp_score

    return total_count

