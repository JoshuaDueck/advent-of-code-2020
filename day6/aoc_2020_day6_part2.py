def main():
    f = open("aoc_2020_day6_input.txt", "r")

    group_members = [[]]
    curr_group = 0

    for line in f:
        if line == '\n':
            curr_group += 1
            group_members.append([])
        else:
            group_members[curr_group].append(line.strip())

    total = 0
    for group in group_members:
        total += len(get_shared_answers(group))

    print(total)


def get_shared_answers(group_list):
    chars = {}
    for member in group_list:
        for char in member:
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1

    common_answers = []
    for char in chars:
        if chars[char] == len(group_list):
            common_answers.append(char)
    
    return common_answers



if __name__ == "__main__":
    main()