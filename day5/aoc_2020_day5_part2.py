def main():
    f = open("aoc_2020_day5_input.txt", "r")

    seat_ids = []

    for boarding_pass in f:
        seat_ids.append(convert_to_seat_id(convert_pass_to_binary(boarding_pass)))

    sorted_ids = sorted(seat_ids)

    # print(sorted_ids)

    prev_id = sorted_ids[0]
    curr_index = 1
    curr_id = sorted_ids[curr_index]

    while curr_id - prev_id <= 1 and curr_index < len(sorted_ids):
        curr_index += 1
        prev_id = curr_id
        curr_id = sorted_ids[curr_index]

    print(f"{prev_id} [ ] {curr_id}")
            


def convert_to_seat_id(seat_address):
    return seat_address[0]*8 + seat_address[1]


def convert_pass_to_binary(pass_string):
    row_string = pass_string[:7]
    col_string = pass_string[7:]

    binary_row_string = ''.join(list(map(char_to_bit, row_string)))
    binary_col_string = ''.join(list(map(char_to_bit, col_string)))

    row_num = int(binary_row_string, 2)
    col_num = int(binary_col_string, 2)

    return [row_num, col_num]


def char_to_bit(char):
    if char == 'F':
        return "0"
    elif char == 'B':
        return "1"
    elif char == 'R':
        return "1"
    elif char == 'L':
        return "0"
    else:
        return ""


if __name__ == "__main__":
    main()