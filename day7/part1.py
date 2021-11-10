def main():
    f = open("test_input.txt", "r") # open bag

    bag_list = {}
    contained_in_list = {}

    for line in f:
        formatted_bag = process_line(line)

        bag_list[formatted_bag['bag_name']] = formatted_bag['contained_bags']
        for bag in formatted_bag['contained_bags']:
            contained_in_list[bag[1]].append() # I stopped here because I need to figure out how we can best 

def process_line(line: str):
    bag_name = get_bag_name(line)
    contained_bags = get_contained_bags(line)

    return {'bag_name': bag_name, 'contained_bags': contained_bags}


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


if __name__ == "__main__":
    main()