NUM_DIC = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "ten": "10"
}


def get_num_from_string(string: str) -> str:
    for key, value in NUM_DIC.items():
        if key in string:
            return value


def day_one(input_file: str) -> int:

    with open(input_file, "r") as f:
        line_list = f.read().split()
    first_digit = ""
    second_digit = ""
    total = 0

    for line in line_list:
        first_builder, second_builder = "", ""
        for i in line:
            first_builder += i
            response = get_num_from_string(first_builder)
            if response is not None:
                first_digit = response
                break
            elif i.isdigit():
                first_digit = i
                break
            else:
                continue

        for x in line[::-1]:
            second_builder += x
            response = get_num_from_string(second_builder[::-1])
            if response is not None:
                second_digit = response
                break
            elif x.isdigit():
                second_digit = x
                break
        total += int(first_digit + second_digit)

    return total
