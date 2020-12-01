### PART 1 ###
# O(n)
f = open("aoc_2020_day1_input.txt", "r")

value_set = set()
for line in f:
    value_set.add(int(line))

f.close()

found_value_pair = [-1,-1]
for value in value_set:
    diff = 2020-value
    if diff in value_set:
        found_value_pair = [value, diff]
        break

print("{} --> {}".format(found_value_pair, found_value_pair[0]*found_value_pair[1])) # [631, 1389] --> 876459


### PART 2 ###
# O(n^2)
found_value_triple = [-1,-1,-1]
for value1 in value_set:
    for value2 in value_set:
        diff = 2020-value1-value2
        if diff in value_set:
            found_value_triple = [diff, value1, value2]
            break

print("{} --> {}".format(found_value_triple, found_value_triple[0]*found_value_triple[1]*found_value_triple[2])) # [1172, 708, 140] --> 116168640