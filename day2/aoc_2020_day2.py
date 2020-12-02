f = open("aoc_2020_day2_input.txt", "r")
# f = ["1-3 a: abcde","1-3 b: cdefg","2-9 c: ccccccccc"]

### PART 1 ###
def valid_pass_p1(password, letter, mincount, maxcount):
    letter_count = 0
    for target_letter in password:
        if target_letter == letter:
            letter_count += 1
    if letter_count >= mincount and letter_count <= maxcount:
        return True
    else:
        return False

### PART 2 ###
def valid_pass_p2(password, letter, pos1, pos2):
    return (password[pos1-1] == letter and not password[pos2-1] == letter) or (password[pos2-1] == letter and not password[pos1-1] == letter)


valid_count = 0
for password_line in f:
    breakdown = password_line.split(":")
    criteria_breakdown = breakdown[0].split(" ")
    min_max = criteria_breakdown[0].split("-")
    if valid_pass_p2(breakdown[-1].strip(), criteria_breakdown[-1], int(min_max[0]), int(min_max[1])):
        valid_count += 1

print(valid_count)