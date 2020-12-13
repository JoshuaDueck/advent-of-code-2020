f = open("aoc_2020_day4_input.txt", "r")

passports = [[]]
curr_passport = 0
for line in f:
    if line == "\n":
        curr_passport += 1
        passports.append([])
    passports[curr_passport].append(line)

print(f"There are {curr_passport} passports.")

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

    print(f"PASSPORT STRING: {joined_passport}\nFLAGS: {flags}")

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


valid_count = 0
for passport in passports:
    if valid_passport(passport):
        valid_count += 1

print(valid_count) # 256 was correct