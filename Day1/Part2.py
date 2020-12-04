from Part1 import target_two_sum

with open('input.txt') as f:
    data = f.read()
report = list(map(int, data.splitlines()))


def three_sum(target, expense_report):
    first_complement = {}
    for element in range(len(expense_report)):
        first_complement[expense_report[element]] = target - expense_report[element]
    print(first_complement)
    for index, element in enumerate(first_complement):
        two_sum = target_two_sum(first_complement[element], expense_report)
        if two_sum is not None:
            return element * two_sum


print(three_sum(2020, report))

sample_input = [
    1721,
    979,
    366,
    299,
    675,
    1456
]

print(three_sum(2020, sample_input) == 241861950)
