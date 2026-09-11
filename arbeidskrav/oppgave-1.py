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


# Oppgave 1.1 - Beregn tids bruk


def oppgave_1_1():
    while True:
        study_sessions = input("\nHow many study session have you had: ")
        study_time = input("How much time have you used in each study sessions: ")

        if not is_int(study_sessions):
            print(
                f"{study_sessions}' is not a whole number. Please enter digits only, e.g. 3."
            )
            continue

        if not is_int(study_time):
            print(
                f"{study_time}' is not a whole number. Please enter digits only, e.g. 3."
            )
            continue

        study_sessions = int(study_sessions)
        study_time = int(study_time)

        if is_positive_int(study_sessions) and is_positive_int(study_time):
            total_minutes = study_time * study_sessions
            hours, minutes = divmod(total_minutes, 60)

            print("\nNumber of study sessions:", study_sessions)
            print("Minutes per session:", study_time)
            print(f"Total study time: {hours} hours and {minutes} minutes")
            break


# Oppgave 1.2 - Analyser tekst


def oppgave_1_2():
    while True:
        analyze_text = input("\nWrite an text here to be analyzed: ")

        # ai recommended this fix at line 55
        if "".join(analyze_text.split()) == "":
            print("Please provide an text and not just spaces")
            continue
        print(
            "\nThis is the amount of charcaters in the text without spaces: ",
            string_counter_without_space(analyze_text),
        )
        print(
            "This is the amount of charcaters in the text with spaces: ",
            len(analyze_text),
        )

        print("This is the text with only small letters:", analyze_text.lower())

        print("This is the text in reverse: ", analyze_text[::-1])

        if "python" in analyze_text.casefold():
            print("This text contains the word python")
        break


# Oppgave 1.3 - Analyser et tallintervall


def oppgave_1_3():
    while True:
        start_value = input("\nPlease provide an start value: ")
        end_value = input("Please provide an end value: ")

        if not is_int(start_value):
            print(
                f"{start_value}' is not a whole number. Please enter digits only, e.g. 3."
            )
            continue
        if not is_int(end_value):
            print(
                f"{end_value}' is not a whole number. Please enter digits only, e.g. 3."
            )
            continue

        start_value = int(start_value)
        end_value = int(end_value)

        if start_value > end_value:
            print("Please enter an start value which is smaller then the end value")
            continue

        even_range = range(start_value, end_value, 2)
        print("\nEvery even number in the range: \n", list(even_range))

        print(
            "This is every number that is dividable by 3: \n",
            int_diversion(start_value, end_value),
        )

        print(
            "This is the sum of every number in the range: \n",
            sum(range(start_value, end_value)),
        )
        break


while True:
    user_input = input(
        "\nThis is an menu for multiple programs:\n 1. for an program to calculate time usage while studying\n 2. for an text analyzer\n 3. for an time interval analyzer\n 4. to exit\n Please enter an value: "
    )

    if not is_int(user_input):
        print(f"{user_input} is not an whole number. Please enter digits e.g 3.")
        continue

    user_input = int(user_input)

    if user_input not in range(1, 5):
        print("Enter an number within the range of 1 to 4, try again.")
        continue

    if user_input == 1:
        oppgave_1_1()
    elif user_input == 2:
        oppgave_1_2()
    elif user_input == 3:
        oppgave_1_3()
    elif user_input == 4:
        break
    else:
        print("Please provide an input!")
