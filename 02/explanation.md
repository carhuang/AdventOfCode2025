# Day 2 Solution Reasoning

## Part 1
The problem statement defines an invalid ID as "any ID which is made only of some sequence of digits repeated twice". This means that an invalid ID:  

- is an integer with an even number of digits
- when split in middle into 2 numbers, the 2 numbers will be identical, such as 55, 6464, 11, etc.

## Part 2
The definition of an invalid ID has been redefined as a positive number "made only of some sequence of digits repeated at least twice". This means that an invalid ID:
- is an integer with more than 1 digit
To further investigate if a number is an invalid ID, we can make use of a sliding window, of which the head index will always be 0, and the tail index can be any number from 1...len(num). With each substring created by the sliding window, we will check:
- firstly, if the len(num) is divisible by len(substring)
- if the substring gets repeated till len(num)