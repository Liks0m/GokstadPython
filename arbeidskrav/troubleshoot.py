import csv

tr_list = []

with open("supporthenvendelser.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        tr_list.append(row)


def sum_resolved_minutes(requests):
    total_list = []
    for request in requests:
        if request["is_resolved"] == "yes":
            total_list.append(int(request["minutes"]))
    total = sum(total_list)
    return total


print(sum_resolved_minutes(tr_list))
