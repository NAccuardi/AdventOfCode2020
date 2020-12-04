with open('input.txt') as f:
    data = f.read()
passwords = list(map(str, data.splitlines()))


def check_passwords(password_list):
    valid_count = 0
    for element in password_list:
        split_line = element.split()
        min_allowed, max_allowed = map(int, split_line[0].split('-'))
        character = split_line[1][0]
        password = split_line[2]

        if min_allowed <= password.count(character) <= max_allowed:
            valid_count += 1

    return valid_count


print(check_passwords(passwords))

zero_matches = [
    "1-3 b: cdefg"
]

one_matches = [
    "1-3 a: abcde"
]

two_matches = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc"
]

print(check_passwords(zero_matches) == 0)
print(check_passwords(one_matches) == 1)
print(check_passwords(two_matches) == 2)
