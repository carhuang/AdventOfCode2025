# Day 7: Laboratories

## Part 1
A beam split occurs when a single downward beam hits a splitter `^`. So, to count the total number of beam splits, we can:
1. iterate through the digram row by row from the top (index `0`), while keeping track of the positions in the row above with a beam
2. if we encounter a splitter `^`, we check if there is a beam right above it. If so, increase the beam split count by 1 and update the new beam position.
3. when we reach the end of the diagram, return the total beam split count.

Here are some observations and possibly assumptions made on the input diagram that I make use of in my code:  
- `S` only appears once and is in row `0` in the diagram.
- the first splitter start to appear on row `2`, so I can start my scan on row `2` of the diagram.
- the splitters never appear in consecutive rows. They are always at least 1 row apart. This means I can step through the diagram 2 rows at a time.

## Part 2
The problem look like it's begging for a DFS + memoization solution. I realize that I can reuse most of my `part1()` logic and tweak the data `beams` store.

Now, instead of using `1`s to keep track of the positions of beams in the current scanning row, I let `beams` keep track of the number of possible route a particle can take at each position. These numbers will get updated as we scan through the diagram from top to bottom row.

After we finish scanning the entire diagram, we can sum up all the final numbers in `beams` to get the total number of routes a single particle from `S` can take.