import random
import function as fn
import subprocess

study_session_storage = []
study_session = {"topic": "", "duration_minutes": 0, "status": ""}

topics = ["Python", "Math", "History", "English", "Physics"]
statuses = ["planned", "completed"]


def example_study_session():
    class ExampleStudySession:
        def __init__(self):
            self.topic = random.choice(topics)
            self.duration_minutes = random.randint(15, 120)
            self.status = random.choice(statuses)

    # on line 25 the error zuban: Incompatible types in assignment (expression has type "int", target has type "str") can just be ignored

    for _ in range(5):
        example = ExampleStudySession()
        session = dict.copy(study_session)
        session["topic"] = example.topic
        session["duration_minutes"] = example.duration_minutes
        session["status"] = example.status
        study_session_storage.append(session)


example_study_session()


def register_study_session():
    while True:
        print("\n Register an study session")
        topic = input("Please state what topic you studied: ")

        if not topic.isalpha():
            print(f"{topic} is not an string, please try again.")
            continue

        duration_minutes = input("Please state how long you studied for: ")

        if not fn.is_int(duration_minutes):
            print(f"{duration_minutes} is not an integer, please try again.")
            continue

        duration_minutes = int(duration_minutes)

        if not fn.is_positive_int(duration_minutes):
            print(f"{duration_minutes} is not an positive integer, please try again.")

        status = input("Please state if the status is planned or completed:")

        if status != "completed" and status != "planned":
            print(f"{status} is not the string completed or planned")
            continue

        session = dict.copy(study_session)

        # on line 64 the error zuban: Incompatible types in assignment (expression has type "int", target has type "str") can just be ignored
        session["topic"] = topic
        session["duration_minutes"] = duration_minutes
        session["status"] = status

        study_session_storage.append(session)

        break


def list_study_sessions(sessions):
    if not sessions:
        print("No study sessions registered yet.")
        return

    for i, sessions in enumerate(sessions, start=1):
        print(
            f"{i}. Topic: {sessions['topic']}, "
            f"Duration: {sessions['duration_minutes']} min, "
            f"Status: {sessions['status']}"
        )


def list_only_completed(sessions):
    if not sessions:
        print("No study sessions registered yet.")
        return

    completed_sessions = []
    for session in sessions:
        if session.get("status") == "completed":
            completed_sessions.append(session)

    if not completed_sessions:
        print("No completed study sessions found.")
    return completed_sessions


def list_search_topic(sessions, search):
    if not sessions:
        print("No study sessions registered yet.")
        return

    search_sessions = []
    for session in sessions:
        if search.lower() in session.get("topic", "").lower():
            search_sessions.append(session)

    if not search_sessions:
        print("No completed study sessions found.")

    return search_sessions


def sum_duration(sessions):

    duration_list = []
    for session in sessions:
        duration_minutes = session.get("duration_minutes")
        duration_list.append(duration_minutes)

    sum_duration = sum(duration_list)
    return sum_duration


def average_duration(sessions):

    duration_list = []
    for session in sessions:
        duration_minutes = session.get("duration_minutes")
        duration_list.append(duration_minutes)

    avg_duration = sum(duration_list) / len(duration_list)
    return avg_duration


# https://discourse.mcneel.com/t/gh-python-convert-integer-time-to-h-m-s/159435/7


while True:
    completed_sessions = list_only_completed(study_session_storage)

    user_input = input(
        "\n This is an menu for storing, logging and analyzing study sessions:\n 1. Register an study session\n 2. Show study sessions\n 3. Show only completed sessions\n 4. Search for an word in the topic\n 5. Sort session after duration with longest first\n 6. Shows collected and average time for completed sessions\n  7. To exit\n Please enter an value: "
    )

    if not fn.is_int(user_input):
        print(f"{user_input} is not an whole number. Please enter digits e.g 3.")
        continue

    user_input = int(user_input)

    if user_input not in range(1, 8):
        print("Enter an number within the range of 1 to 7, try again.")
        continue

    #    https://www.reddit.com/r/learnpython/comments/1b4sk5n/how_to_clear_a_console_in_python/
    subprocess.call("clear")

    if user_input == 1:
        register_study_session()
    elif user_input == 2:
        list_study_sessions(study_session_storage)
    elif user_input == 3:
        list_study_sessions(completed_sessions)
    elif user_input == 4:
        while True:
            search = input("Please input what to search for: ")

            if not search.isalpha():
                print(f"{search} is not an string, please try again.")
                continue

            search_topics = list_search_topic(study_session_storage, search)
            list_study_sessions(search_topics)
            break
    elif user_input == 5:
        desending = fn.desending_list(study_session_storage)
        list_study_sessions(desending)
    elif user_input == 6:
        collective_duration = sum_duration(completed_sessions)
        avg_duration = average_duration(completed_sessions)

        print(
            "\nThe total study time duration is",
            fn.convert_int_to_hms(collective_duration),
        )

        print(
            "The average study session lasts for", fn.convert_int_to_hms(avg_duration)
        )

    elif user_input == 7:
        subprocess.call("clear")
        break
    else:
        print("Please provide input")

    if user_input != 7:
        input("\nPress enter to continue...")
        subprocess.call("clear")
