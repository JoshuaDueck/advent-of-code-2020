def main():
    f = open("aoc_2020_day6_input.txt", "r")

    groups = ['']
    curr_group = 0

    for line in f:
        if line == '\n':
            curr_group += 1
            groups.append('')
        else:
            groups[curr_group] += line.strip()
    
    total = 0
    for group in groups:
        total += count_unique_chars(group)

    print(total)


def count_unique_chars(group_string):
    chars = {}
    count = 0
    for char in group_string:
        if char not in chars:
            chars[char] = True
            count += 1
    
    return count

if __name__ == "__main__":
    main()