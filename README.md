An algorithm adventure to save Christmas!



### Warning: Spoilers Below:
[Day 1 Solution](https://github.com/JoshuaDueck/advent-of-code-2020/tree/main/day1)

*Part 1: O(n)*

*Part 2: O(n<sup>2</sup>)*
- Part 1 involved adding all items to a set, then looping through the set once, subtracting the current value from 2020, then checking if the difference is in the set.
- Part 2 involved the same setup, but used an inner loop so we could subtract value1 and value2 from 2020, then checking if the difference is in the set. It may be possible to do it faster, I did not look for a better solution.


[Day 2 Solution](https://github.com/JoshuaDueck/advent-of-code-2020/tree/main/day2)

*Part 1: O(mn), m = number of letters in a password*

*Part 2: O(n)*
- Part 1 involved checking the valid password by counting the number of times the target letter appears in the string, then checking if it falls in the bounds.
- Part 2 involved the same setup, but this time I didn't need to loop through the whole string, I just checked the indices and returned the appropriate boolean result.


[Day 3 Solution](https://github.com/JoshuaDueck/advent-of-code-2020/tree/main/day3)

*Part 1: O(n)*

*Part 2: O(n)*
- Part 1 and part 2 were nearly identical, but with different increments on the coordinates. I wrote the code very quickly without thinking it through a whole lot, which is why it ended up being so messy and repetitive. In reality, I could have created a function and simply used this. Perhaps I will do that sometime in the future, but I just wanted to get this done so I could move on to my real homework haha. In total it took me a little under 10 minutes to do everything.
