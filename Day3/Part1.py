with open('input.txt') as f:
    data = f.read()
mountain = list(map(str, data.splitlines()))


def tree_checker(hillside, right, down):

    collisions = current_x = current_y = 0

    while current_y < len(hillside):
        if hillside[current_y][current_x % len(hillside[0])] == '#':
            collisions += 1
        current_y += down
        current_x += right

    return collisions


print(tree_checker(mountain, 3, 1))
