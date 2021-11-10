import re

def main():
    f = open("test_input.txt", "r")

    # each bag name is a key, we have 2 dicts: one for parents, one for children.
    # when we add a new bag, we add its direct children to the children dict for that bag
    # when we add a new child for a bag, we add it's parent to the parent dict for that child
    # when we search for a bag's parents, simply use the parents dict to search through [shiny gold]'s parents, and their parents, and onwards.

    bag_specs = []
    for line in f:
        bag_specs.append(extract_bags_from_line(line))

    print(find_all_parents('shiny gold', make_children_and_parents(bag_specs)[1], []))


def extract_bags_from_line(line):
    bag_and_contained = line.split("contain")
    target_bag = bag_and_contained[0].strip()[:-5] # very contingent on having " bags" as the last 5 characters.
    contained_bags = bag_and_contained[1].strip()

    contained_bags = list(map(sanitize_bags, contained_bags.split(",")))

    return [target_bag, contained_bags]

def make_children_and_parents(specs):
    bag_children = {}
    bag_parents = {}

    for bag in specs:
        for child in bag[1]:
            if bag[0] not in bag_children:
                bag_children[bag[0]] = []
            bag_children[bag[0]].append(child)
    
    for bag in specs:
        for child in bag[1]:
            if child not in bag_parents:
                bag_parents[child] = []
            bag_parents[child].append(bag[0])

    return [bag_children, bag_parents]


def find_all_parents(bag, all_parents, current_list):
    if bag in all_parents:
        current_list.append(bag)
        for parent in all_parents:
            find_all_parents(parent, all_parents, current_list)
        return current_list
    else:
        return None


def sanitize_bags(bag_string):
    stripped = bag_string.strip()
    no_bags = stripped[:stripped.find(" bag")]
    match = re.search("[0-9]+", no_bags)
    if match != None:
        return no_bags[match.end():].strip()
    return 


if __name__ == "__main__":
    main()