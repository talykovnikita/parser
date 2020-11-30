import re
import sys


def is_contains_coordinates(log_line: list) -> bool:
    COORD_TEMPLATE = r'\[[0-9]{2}.[0-9]{6}, [0-9]{2}.[0-9]{6}\]'
    if re.findall(COORD_TEMPLATE, log_line):
        return True

    return False


def clear_log_line(log_line: list) -> str:
    split_line = log_line.split()
    return f"{split_line[0]} {split_line[1]} {split_line[2]} {split_line[-1][:-1]}, {split_line[-2][1:-1]}"


def parse_log(file_input: str, file_output: str = "to_developer.txt") -> None:
    try:
        with open(file_input, "r") as orig_log, open(file_output, "w") as new_log:
            for line in orig_log.readlines():
                if is_contains_coordinates(line):
                    new_log.write(f"{clear_log_line(line)}\n")
    except FileNotFoundError:
        print(f"File {file_input} was not find. Please, check your input.")
        print_info()


def print_info():
    print(f"Usage: python {sys.argv[0]} file_for_parsing.txt")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        parse_log(sys.argv[1])
    else:
        print_info()
