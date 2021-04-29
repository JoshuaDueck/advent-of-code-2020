import re

f = open("aoc_2020_day4_input.txt", "r")

passports = [[]]
curr_passport = 0
for line in f:
    if line == "\n":
        curr_passport += 1
        passports.append([])
    else:
        passports[curr_passport].append(line)

def valid_passport(passport):
    joined_passport = ""
    for line in passport:
        joined_passport = joined_passport + line

    flags={
        "byr":False,
        "iyr":False,
        "eyr":False,
        "hgt":False,
        "hcl":False,
        "ecl":False,
        "pid":False
    }

    flags["byr"] = "byr" in joined_passport
    flags["iyr"] = "iyr" in joined_passport
    flags["eyr"] = "eyr" in joined_passport
    flags["hgt"] = "hgt" in joined_passport
    flags["hcl"] = "hcl" in joined_passport
    flags["ecl"] = "ecl" in joined_passport
    flags["pid"] = "pid" in joined_passport

    key_values = split_into_key_values(joined_passport)
    print(key_values)

    for flag in flags:
        if not flags[flag]:
            return False

    for key in key_values:
        try:
            int_val = int(key_values[key])
        except ValueError:
            int_val = None
        val = key_values[key]
        if key == "byr":
            if int_val < 1920 or int_val > 2002:
                return False 
        elif key == "iyr":
            if int_val < 2010 or int_val > 2020:
                return False
        elif key == "eyr":
            if int_val < 2020 or int_val > 2030:
                return False
        elif key == "hgt":
            cm_loc = val.find('cm')
            in_loc = val.find('in')
            if cm_loc != -1:
                # working in cm
                number = int(val[:cm_loc])
                if number < 150 or number > 193:
                    return False
            elif in_loc != -1:
                # working in in
                number = int(val[:in_loc])
                if number < 59 or number > 76:
                    return False
            else:
                # could not find a unit, invalid
                return False
        elif key == "hcl":
            if re.search('#[0-9A-Fa-f]{6}', val) == None:
                return False
        elif key == "ecl":
            if not (
                val == 'amb'
                or val == 'blu'
                or val == 'brn'
                or val == 'gry'
                or val == 'grn'
                or val == 'hzl'
                or val == 'oth'
            ):
                return False
        elif key == "pid":
            if re.search('^[0-9]{9}$', val) == None:
                return False

    return True


def split_into_key_values(passport_string):
    key_values = {}
    index = 0
    next_break = 0

    while index > -1 and next_break > -1:
        index = passport_string.find(':')
        next_space = passport_string.find(' ')
        next_newline = passport_string.find('\n')

        if next_newline != -1 and next_space != -1:
            next_break = min(next_space, next_newline)
        elif next_newline == -1 and next_space != -1:
            next_break = next_space
        elif next_space == -1 and next_newline != -1:
            next_break = next_newline
        else:
            next_break == -1 # both not found

        key = passport_string[index-3:index]
        value = passport_string[index+1:next_break]
        
        if key != '' and value != '':
            key_values[key] = value
        
        passport_string = passport_string[next_break+1:]

    return key_values

valid_count = 0

for passport in passports:
    if valid_passport(passport):
        valid_count += 1

print(valid_count) # 256 was correct for part 1
                   # 198 was correct for part 2