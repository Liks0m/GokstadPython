from operator import itemgetter


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


def desending_list(sessions):
    desending_list = sorted(sessions, key=itemgetter("duration_minutes"), reverse=True)
    return desending_list


def convert_int_to_hms(value):
    value = float(value)
    seconds = value * 60
    m, s = divmod(seconds, 60)
    s = round(s)
    h, m = divmod(m, 60)
    a = "%dh:%02dm:%02ds" % (h, m, s)
    return a
