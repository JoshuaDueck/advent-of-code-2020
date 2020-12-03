f = open("aoc_2020_day2_input.txt", "r")

line_list = f.readlines()

curr_tile = [0,0]
tree_count_3_1 = 0
for line in line_list:
    if line[curr_tile[0]] == "#":
        tree_count_3_1 += 1
    curr_tile = [(curr_tile[0]+3)%31, curr_tile[1]+1]

print(tree_count_3_1)

curr_tile = [0,0]
tree_count_1_1 = 0
for line in line_list:
    if line[curr_tile[0]] == "#":
        tree_count_1_1 += 1
    curr_tile = [(curr_tile[0]+1)%31, curr_tile[1]+1]

print(tree_count_1_1)

curr_tile = [0,0]
tree_count_5_1 = 0
for line in line_list:
    if line[curr_tile[0]] == "#":
        tree_count_5_1 += 1
    curr_tile = [(curr_tile[0]+5)%31, curr_tile[1]+1]

print(tree_count_5_1)

curr_tile = [0,0]
tree_count_7_1 = 0
for line in line_list:
    if line[curr_tile[0]] == "#":
        tree_count_7_1 += 1
    curr_tile = [(curr_tile[0]+7)%31, curr_tile[1]+1]

print(tree_count_7_1)

curr_tile = [0,0]
tree_count_1_2 = 0
while curr_tile[1] < len(line_list):
    if line_list[curr_tile[1]][curr_tile[0]] == "#":
        tree_count_1_2 += 1
    curr_tile = [(curr_tile[0]+1)%31, curr_tile[1]+2]

print(tree_count_1_2)

print("ANSWER: {}".format(tree_count_3_1*tree_count_1_1*tree_count_5_1*tree_count_7_1*tree_count_1_2))