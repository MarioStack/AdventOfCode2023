from typing import Tuple


def extract_numeric_values(grid: list[str], coordinates: set[Tuple[int, int]]) -> list[int]:
    ns = []
    for row, col in coordinates:
        value = ""
        for char in grid[row][col:]:
            if char.isdigit():
                value += char
            else:
                break
        ns.append(int(value))
    return ns


def day_three(input_file: str) -> int:
    with open(input_file, "r") as file:
        grid = file.read().splitlines()

    total = 0

    for row_index, row in enumerate(grid):
        for col_index, char in enumerate(row):
            if char != "*":
                continue

            coordinates = set()

            for cr in [row_index - 1, row_index, row_index + 1]:
                for cc in [col_index - 1, col_index, col_index + 1]:
                    if cr < 0 or cr >= len(grid) or cc < 0 or cc >= len(grid[cr]) or not grid[cr][cc].isdigit():
                        continue
                    while cc > 0 and grid[cr][cc - 1].isdigit():
                        cc -= 1
                    coordinates.add((cr, cc))

            if len(coordinates) == 2:
                numeric_values = extract_numeric_values(grid, coordinates)
                total += numeric_values[0] * numeric_values[1]

    return total
