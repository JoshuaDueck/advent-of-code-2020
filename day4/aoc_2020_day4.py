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

    split_into_key_values(joined_passport)

    for flag in flags:
        if not flags[flag]:
            return False
        else:
            value_start = joined_passport.find(flag+':')+4
            if flag == "byr":
                pass
            elif flag == "iyr":
                pass
            elif flag == "eyr":
                pass
            elif flag == "hgt":
                pass
            elif flag == "hcl":
                pass
            elif flag == "ecl":
                pass
            elif flag == "pid":
                pass

    return True


def split_into_key_values(passport_string):
    index = 0
    next_break = 0
    print(f"=== REPORT FOR\n{passport_string}\n===")
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
            # they're both not found
            next_break == -1

        key = passport_string[index-3:index]
        value = passport_string[index+1:next_break]

        passport_string = passport_string[next_break+1:]
        print(f"{key} $ {value}, ")
    print(f"=== END REPORT ===")

valid_count = 0

for passport in passports:
    if valid_passport(passport):
        valid_count += 1

print(valid_count) # 256 was correct