# Day 4: Printing Department

## Part 1
I'm going with the brute-force approach to solve part 1 -- iterating through each position in the map from top left to bottom right. When rolls of paper `@` is encountered, calculate the number of rolls of paper in its eight adjacent positions. If the number is smaller than 4, add 1 to the counter. Return the final counter number when the entire map has been checked.

## Part 2
In part 2, I repeated the same brute-force approach in part 1 to find the accessible rolls of paper in each round. The most tricky part for me is to find a way to terminate the while-loop in my `part2()`. The problem instructs to "stop once no more rolls of paper are accessible by a forklift", which means the while-loop should terminate once the current round ends with number of accessible papers = 0. But, I cannot simply make the exit condition for the while-loop be `removed == 0` because that could also mean that no checking has been done yet. In the end, I added another variable `prev-removed` to keep track of the number of removed paper rolls before the current round and use it to test the exit condition.