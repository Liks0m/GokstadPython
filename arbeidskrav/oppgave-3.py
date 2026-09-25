import function as fn
import datetime as dt

dt1 = dt.datetime(2066, 10, 24, 12, 36, 9)
dt2 = dt.datetime(2020, 3, 12, 12, 36, 9)
dt3 = dt.datetime(1900, 7, 18)
dt4 = dt.datetime(2004, 3, 22)
dt5 = dt.datetime(2026, 8, 28, 6, 35)

date_list = [dt1, dt2, dt3, dt4, dt5]


# https://discuss.python.org/t/best-way-to-validate-an-entered-date/49406/3
def validate_dates(date):
    try:
        date = dt.datetime.strptime(date, "%d.%m.%Y")
        return date
    except ValueError:
        print("\n" + f"{date} is not an valid date in the format (dd.mm.yyyy)")


# https://www.pythonmorsels.com/datetime-arithmetic/


def validate_time(start_time):
    try:
        start_time = dt.datetime.strptime(start_time, "%H:%M")
        return start_time
    except ValueError:
        print("\n" + f"{start_time} is not in the format of the 24 hour clock")


def calculate_end_time(date, start_time, duration):
    combined_date = fn.sum_date_times([date, start_time])

    duration = dt.timedelta(minutes=duration)

    end_time = duration + combined_date

    return end_time


def calculate_two_days(date1, date2):
    date = abs(date1 - date2)
    return date


def chronological_list(list):
    list.sort(reverse=False)
    return list


while True:
    date_one = input("\n" + "Please enter an date in the format (dd.mm.yyyy): ")
    date_two = input("Please enter an second date in the format (dd.mm.yyyy): ")
    start_time = input("Please enter an start time with 24 hour clock format: ")
    duration = input("Please enter the duration of the study session: ")

    if not fn.is_int(duration):
        print(f"{duration} is not an integer, please try again.")
        continue

    duration = int(duration)

    if not fn.is_positive_int(duration):
        print(f"{duration} is not an positive integer, please try again.")
        continue

    if not validate_dates(date_one):
        continue

    if not validate_dates(date_two):
        continue

    if not validate_time(start_time):
        continue

    date_one = validate_dates(date_one)
    date_two = validate_dates(date_two)
    start_time = validate_time(start_time)

    print(
        "\nThis function takes start time and duration and calculates end time:\n",
        calculate_end_time(date_one, start_time, duration),
    )

    print(
        f"\nThis function takes two dates and calculates an positive amount of dates between the two date {date_one:%d.%m.%Y} and {date_two:%d.%m.%Y}:\n",
        calculate_two_days(date_one, date_two),
    )

    print(
        "\nThis list takes an list with dates and returns an chronologically sorted list of dates:\n",
        chronological_list(date_list),
    )
    break


# https://docs.python.org/3/library/datetime.html
# https://docs.python.org/3/howto/sorting.html
