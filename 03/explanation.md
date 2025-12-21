# Day 3: Lobby

## Part 1
We are asked to find out the largest combination of double-digit number from each line in the input, while preserving the order of the digits. Observe that:
- the first digit can be any digit at index 0...n-1, and the second digit can be any digit from 1...n
- in order to make the largest double-digit number, we should prioritize maximizing the first digit
- after finding the maximum first digit, we can go on to find the maximum number from index(first digit)...index(n)

## Part 2
The logic to the solution doesn't change much, except now we need to find the largest combination of *12-digit* number.
- the first digit can be any digit at index 0...n-11, the second digit can be any digit at index 1...n-10, the third digit can be any digit at index 2...n-9, and so on
- similarly to part 1, we should prioritize maximizing the most significant digits

Since the logic of part 1 and part 2 are so similar, I've refactored the code of part 1 to introduce a new field in get_max_joltage() that takes into account of the number of digits expected in the joltage of each bank.