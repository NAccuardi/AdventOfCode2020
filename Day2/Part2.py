with open('input.txt') as f:
    data = f.read()
passwords = list(map(str, data.splitlines()))


def check_passwords_location(password_list):
    valid_count = 0
    for element in password_list:
        split_line = element.split()
        first_pos, second_pos = map(int, split_line[0].split('-'))
        character = split_line[1][0]
        password = split_line[2]
        if (password[first_pos-1] == character) != (password[second_pos-1] == character):
            valid_count += 1

    return valid_count


print(check_passwords_location(passwords))
