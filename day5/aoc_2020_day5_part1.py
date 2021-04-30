def main():
    f = open("aoc_2020_day5_input.txt", "r")

    rows_and_columns = []

    for boarding_pass in f:
        rows_and_columns.append(convert_pass_to_binary(boarding_pass))
        print(convert_pass_to_binary(boarding_pass))
    
    print(find_biggest_seat_id(rows_and_columns))


def find_biggest_seat_id(seat_passes):
    largest_id = -1

    for seat_address in seat_passes:
        seat_id = seat_address[0]*8 + seat_address[1]
        largest_id = max(largest_id, seat_id)
    
    return largest_id


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