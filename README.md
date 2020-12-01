An algorithm adventure to save Christmas!



### Warning: Spoilers Below:
[Day 1 Solution](https://github.com/JoshuaDueck/advent-of-code-2020/tree/main/day1)
*Part 1: O(n)
Part 2: O(n<sup>2</sup>)*
- Part 1 involved adding all items to a set, then looping through the set once, subtracting the current value from 2020, then checking if the difference is in the set.
- Part 2 involved the same setup, but used an inner loop so we could subtract value1 and value2 from 2020, then checking if the difference is in the set. It may be possible to do it faster, I did not look for a better solution.
