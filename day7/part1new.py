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
    print(len(get_possible_containers("shiny gold", bag_contained_by=bag_contained_by))) # 296 -- correct

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

# a wrapper functin for get_possible_containers
def get_possible_containers(bag_name, bag_contained_by):
    return __get_possible_containers(bag_name, bag_contained_by[bag_name], bag_contained_by)

def __get_possible_containers(bag_name: str, containing_bags: list, bag_contained_by: dict):
    bags_containing_target = bag_contained_by[bag_name]

    if containing_bags == []:
        return bags_containing_target
    else:
        for bag in bags_containing_target:
            possible_containers = __get_possible_containers(bag, bags_containing_target, bag_contained_by)

            for possible_container in possible_containers:
                if possible_container not in bags_containing_target:
                    bags_containing_target.append(possible_container)

    return bags_containing_target

if __name__ == "__main__":
    main()