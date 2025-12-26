# Day 5: Cafeteria

from sortedcontainers import SortedDict, SortedList

# read the ranges
with open('./ranges.txt', 'r') as f:
  lines = f.readlines()
  ranges = [entry.strip() for entry in lines]

# read the ids
with open('./ids.txt', 'r') as f:
  lines = f.readlines()
  ids = [int(entry.strip()) for entry in lines]

# parse the ranges
db = SortedDict()

# merge ranges when start > db_key
def merge_prev_ranges(start, end, db_key):
  if start > db[db_key] + 1:
    db[start] = end
  else:
    db[db_key] = max(db[db_key], end)

# merge ranges when start < db_key
def merge_next_ranges(start, end, db_key):
  if end < db_key - 1:
    db[start] = end
  else:
    db[start] = max(end, db[db_key])
    del db[db_key]

# parse ranges
for line in ranges:
  start, end = map(int, line.split('-'))
  skv = SortedList(db.keys())
  # if no ranges yet
  if len(skv) == 0:
    db[start] = end
    continue
  # find the first range with start >= current start
  boundary = skv.bisect_left(start)
  # current start is bigger than all existing range-starts
  if boundary == len(skv):
    merge_prev_ranges(start, end, skv[-1])
  # current start is equal to boundary key
  elif start == skv[boundary]:
    db[start] = max(end, db[skv[boundary]])
    if boundary + 1 < len(skv):
      merge_next_ranges(start, db[start], skv[boundary+1])
  # current start is smaller than boundary key
  else:
    if boundary > 0:
      merge_prev_ranges(start, end, skv[boundary-1])
      # update start and end after potential merging with previous range
      if not db.__contains__(start):
        start = skv[boundary-1]
        end = db[start]
    merge_next_ranges(start, end, skv[boundary])

def is_fresh(id, skv):
  boundary = skv.bisect_left(id)
  # id > all range starts
  if boundary == len(skv):
    return id <= db[skv[-1]]
  # id == boundary range start
  elif id == skv[boundary]:
    return True
  # id < all range starts
  elif boundary == 0:
    return False
  # id < boundary range start
  else:
    prev = skv[boundary - 1]
    return prev <= id <= db[prev]

def part1():
  skv = SortedList(db.keys())
  fresh = 0
  for food in ids:
    fresh += is_fresh(food, skv)
  return fresh

def part2():
  total = 0
  for key in db.keys():
    total += db[key] - key + 1
  return total

# print("Part 1:", part1())
print("Part 2:", part2())