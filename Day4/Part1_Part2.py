import re

passports = []


def valid_field(ky, val):
    print(ky, val)
    if ky == 'byr' and 1920 <= int(val) <= 2002:
        return True
    if ky == 'iyr' and 2010 <= int(val) <= 2020:
        return True
    if ky == 'eyr' and 2020 <= int(val) <= 2030:
        return True
    if ky == 'hgt':
        if val.endswith('cm') and 150 <= int(val[:-2]) <= 193 \
                or val.endswith('in') and 59 <= int(val[:-2]) <= 76:
            return True
    if ky == 'hcl' and re.match('#[0-9a-f]{6}', val):
        return True
    if ky == 'ecl' and val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    if ky == 'pid' and len(val) == 9:
        return True
    if ky == 'cid':
        return True
    return False


with open('input.txt') as f:
    temp_dict = {}
    for line in f:
        if line not in ['\n', '\r\n']:
            line = line.rstrip('\n')
            split_lines = line.split()
            for element in split_lines:
                key, value = element.split(':')
                if valid_field(key, value):
                    temp_dict[key] = value
        else:
            passports.append(temp_dict.copy())
            temp_dict.clear()
    else:
        passports.append(temp_dict.copy())


def check_passports(passports_to_check):
    valid_passports = 0
    for port in passports_to_check:
        if len(port.keys()) == 8:
            valid_passports += 1
        if len(port.keys()) == 7 and 'cid' not in port.keys():
            valid_passports += 1
    return valid_passports


print(check_passports(passports))
