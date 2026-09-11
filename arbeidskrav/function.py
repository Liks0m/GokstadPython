def is_int(text):
    if text.isdigit():
        return True
    if text.startswith("-") and text[1:].isdigit():
        return True
    return False


def is_positive_int(value):
    return value > 0


# https://stackoverflow.com/questions/8270092/remove-all-whitespace-in-a-string
def string_counter_without_space(text):
    string_without_spaces = "".join(text.split())
    string_counter = len(string_without_spaces)
    return string_counter


# https://www.geeksforgeeks.org/python/python-program-to-print-all-the-numbers-divisible-by-3-and-5-for-a-given-number/ and revised with claude to fit into my py program
def int_diversion(start, end):
    numbers = []
    for num in range(start, end):
        if num % 3 == 0:
            numbers.append(num)
    return numbers
