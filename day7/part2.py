def main():
    f = open("input.txt", "r") # open bag

    bag_contents = {}
    bag_contained_by = {}

    for line in f:
        bag_name = get_bag_name(line)
        contained_bags = get_contained_bags(line)

        bag_contents[bag_name] = contained_bags
        for contained_bag in contained_bags:
            if contained_bag[1] not in bag_contained_by:
                bag_contained_by[contained_bag[1]] = []
            if bag_name not in bag_contained_by:
                bag_contained_by[bag_name] = []

            bag_contained_by[contained_bag[1]].append(bag_name)
    
    f.close()
    print(get_num_contained("shiny gold", bag_contents))

# a function that pretty-prints a dictionary of lists
def print_dict(dictionary: dict):
    for key in dictionary:
        print(key, ":", dictionary[key])

def get_bag_name(line: str):
    bags_index = line.find("bags")

    return line[0:bags_index].strip()

def get_contained_bags(line: str):
    bag_array_start = line.find("contain")
    bag_array_start += len("contain ")

    bag_string = line[bag_array_start:]

    if "no other bags" in bag_string:
        return []
    else:
        bag_string = bag_string[:-2]
        bag_string_split = bag_string.split(", ")
        bag_array = []

        for bag in bag_string_split:
            bag_word_index = bag.find(" bag")
            bag = bag[:bag_word_index]
            bag_split = bag.split(" ")
            try:
                bag_array.append((int(bag_split[0]), " ".join(bag_split[1:])))
            except:
                print("Error: Bad integer format!")
        
        return bag_array


def get_num_contained(bag_name: str, bag_contents: dict):
    return __get_num_contained(bag_name, bag_contents[bag_name], bag_contents)

def __get_num_contained(bag_name: str, contained_bags: list, bag_contents: dict):
    bags_in_target = bag_contents[bag_name]

    if contained_bags == []:
        return bags_in_target
    else:
        print(bag_contents['clear blue'])
        for bag in bag_contents[bag_name]:
            possible_bags = __get_num_contained(bag[1], bags_in_target, bag_contents)

            bags_in_target.append(possible_bags)

if __name__ == "__main__":
    main()