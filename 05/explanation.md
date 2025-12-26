## Part 1
The obvious brute-force solution that first popped into my mind is to go through the given ranges and generate all the ids specified by each range. The generated ids will be appended into a `set` to avoid duplicates. However, the number ranges given in `ranges.txt` are quite large, and I worry that my brute-force solution will be too slow.

So, the second approach is to create a `db` from the ranges input and try to consolidate all the ranges into a Python `dict`. The dictionary consists of key, value pairs where the key is a unique integer representing the start of a range, and the value is a unique integer representing the end of a range. The `db`'s keys should be sorted in increasing order at all times. Python3 doesn't have a native sorted dictionary data structure, so I will have to use the third-party library `sortedcontainers` to achieve O(log n) insertion and lookup for `db`.

This is how I parse the ranges input -- I loop through all ranges input and extract the `start` and `end` number of each ranch input. For each range,
- if current `db` is empty, simply add the current range to `db`
- else, find the first range in `db` with key >= `start`, called the boundary range.
- if no boundary range is found, this means that `start` is bigger than all key values in `db`. In this case, find out if we need to merge the current range with the tail range in `db`, `db[-1]`. If not, add the current range to `db`.
- else if `start` == the boundary range key, make db[start] = max(end, db[start]), and then check if we need to merge the current range with the next range, if the next range exists
- else, we know that the boundary range key > `start`. Check if we need to merge current range with the range before boundary range (if it exists), then check if we need to merge the resulting range with the boundary range.

I find this logic buggy to implement and had to make use of a test ranges file.

If I were to do it again, I would try using an Interval Tree data structure to store the ranges.

