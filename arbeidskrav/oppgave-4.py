import csv
import function as fn
from dataclasses import dataclass
from collections import Counter
import datetime as dt


@dataclass
class SupportRequest:
    id: str
    category: str
    minutes: str
    is_resolved: str


# task 4.1
case_list = []

with open("supporthenvendelser.csv", newline="") as support_request:
    reader = csv.DictReader(support_request)
    for row in reader:
        case_list.append(SupportRequest(**row))


def is_valid_request(support_request):

    if not fn.is_int(support_request.id) or not fn.is_positive_int(
        int(support_request.id)
    ):
        return False
    if support_request.category == "":
        return False
    if not fn.is_int(support_request.minutes) or not fn.is_positive_int(
        int(support_request.minutes)
    ):
        return False
    if support_request.is_resolved != "yes" and support_request.is_resolved != "no":
        return False
    return True


def field_error(support_requests):

    for support_request in support_requests:
        if fn.is_int(support_request.id):
            id = int(support_request.id)

        if support_request.category == "":
            print(f"The field with id-number: {id} has an empty category field")

        if not fn.is_positive_int(id):
            print(
                f"The field with id-number: {id} does not contain an ID that has an postive integer"
            )

        if not fn.is_int(support_request.minutes):
            print(f"The field with id-number: {id} has an invalid minutes field")

        if support_request.is_resolved != "yes" and support_request.is_resolved != "no":
            print(
                f"The field with id-number: {id} has an is_resolved field which does not state yes or no"
            )


def validate_list(support_requests):

    valid_requests = []
    for request in support_requests:
        if is_valid_request(request):
            valid_requests.append(request)
    return valid_requests


field_error(case_list)

case_list = validate_list(case_list)

# task 4.2


def category_counter(support_requests):
    return Counter(r.category for r in support_requests)


def case_status_counter(support_requests):
    return Counter(r.is_resolved for r in support_requests)


def time_list(support_requests):

    time_list = []
    for support_request in support_requests:
        if support_request.minutes:
            time_delta = dt.timedelta(minutes=int(support_request.minutes))
            time_list.append(time_delta)
    return time_list


def unresolved_cases(support_request):
    return support_request.is_resolved == "no"


unresolved_list = list(filter(unresolved_cases, case_list))
sorted_list = sorted(unresolved_list, key=lambda m: int(m.minutes), reverse=True)


def prettier_unresolved_list(sorted_list, f):

    for i, sorted_list in enumerate(sorted_list, start=1):
        f.write(
            f"\n{i}. ID: {sorted_list.id}\n"
            f"Category: {sorted_list.category}\n"
            f"Minutes: {sorted_list.minutes}\n"
            f"Is resolved: {sorted_list.is_resolved}\n"
        )


def file_writer():
    category_dict = category_counter(case_list)
    time_avg_sum = time_list(case_list)
    resolved_dict = case_status_counter(case_list)
    avg = sum(time_avg_sum, dt.timedelta(0, 0)) / len(time_avg_sum)
    avg_hours = avg.total_seconds() / 3600

    with open("support_rapport.txt", "w") as f:
        print("number of valid cases and number in each category:", file=f)

        print("\n" + "The amount of support_requests are", len(case_list), file=f)

        print(
            "The amonut of cases within the category of innlogging is",
            category_dict["innlogging"],
            "\n" + "The amonut of cases within the category of programvare is",
            category_dict["programvare"],
            "\n" + "The amonut of cases within the category of nettverk is",
            category_dict["nettverk"],
            "\n" + "The amonut of cases within the category of utstyr is",
            category_dict["utstyr"],
            "\n",
            file=f,
        )

        print(
            "total and average time spent, with averages to one decimal place:", file=f
        )

        print(
            "\nThe total time of all cases is",
            sum(time_avg_sum, dt.timedelta(0, 0)),
            "\n" + "The average time of all cases in one decimal place is",
            f"{avg_hours:.1f}",
            "\n",
            file=f,
        )

        print("number of resolved and unresolved cases:", file=f)

        print(
            "\nThe amount of resolved cases are",
            resolved_dict["yes"],
            "\n" + "The amount of unresolved cases are",
            resolved_dict["no"],
            "\n",
            file=f,
        )

        print(
            "the category with the most cases:",
            file=f,
        )

        print(
            "\nThe category with the most amount of cases is",
            max(category_dict, key=category_dict.get),
            file=f,
        )

        print(
            "\nunresolved cases sorted with the most time-consuming one first:", file=f
        )

        prettier_unresolved_list(sorted_list, f)


file_writer()
