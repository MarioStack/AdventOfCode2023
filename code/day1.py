num_dic = {
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


def get_num_from_string(string):
    for i in num_dic:
        if i in string:
            return num_dic[i]


def day_one(input_file):

    with open(input_file, "r") as f:
        line_list = f.read().split()

    first_digit = ""
    second_digit = ""
    total = 0

    for line in line_list:
        first_builder = ""
        second_builder = ""
        for i in line:
            first_builder = first_builder + i
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
            second_builder = second_builder + x
            response = get_num_from_string(second_builder[::-1])
            if response is not None:
                second_digit = response
                break
            elif x.isdigit():
                second_digit = x
                break
            else:
                continue
        total += int(first_digit + second_digit)

    return total
