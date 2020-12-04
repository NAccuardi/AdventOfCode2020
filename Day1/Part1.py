with open('input.txt') as f:
    data = f.read()
report = list(map(int, data.splitlines()))


def target_two_sum(target, expense_report):
    temp = {}
    for element in range(len(expense_report)):
        complement = target - expense_report[element]
        if complement in temp:
            return complement * expense_report[element]
        else:
            temp[expense_report[element]] = element


print(target_two_sum(2020, report))

sample_input = [
    1721,
    979,
    366,
    299,
    675,
    1456
]

print(target_two_sum(2020, sample_input) == 514579)
print(target_two_sum(2020, report) == 651651)
