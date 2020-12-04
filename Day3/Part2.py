from Part1 import tree_checker

with open('input.txt') as f:
    data = f.read()
mountain = list(map(str, data.splitlines()))


def route_checker(hillside,slopes):
    tree_impacts = 1
    for slope in slopes:
        tree_impacts *= tree_checker(hillside, slope[0], slope[1])
    return tree_impacts


slopes_to_check = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

print(route_checker(mountain, slopes_to_check))
