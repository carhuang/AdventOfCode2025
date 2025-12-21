# Day 4: Printing Department

# read the input
with open('./input.txt', 'r') as f:
  lines = f.readlines()
  grid = [list(entry.strip()) for entry in lines]

def has_paper(r, c):
  if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
    return False
  return grid[r][c] == '@'

def is_accessible(r, c):
  paper_count = 0
  # look up
  paper_count += has_paper(r - 1, c) + has_paper(r - 1, c - 1) + has_paper(r - 1, c + 1)
  # look down
  paper_count += has_paper(r + 1, c) + has_paper(r + 1, c - 1) + has_paper(r + 1, c + 1)
  # look left and right
  paper_count += has_paper(r, c - 1) + has_paper(r, c + 1)
  return paper_count < 4

def remove_paper(positions):
  for r, c in positions:
    grid[r][c] = '.'
  return

def part1():
  accessible = 0
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == '@' and is_accessible(r, c):
        accessible += 1
  return accessible

def part2():
  prev_removed = -1
  removed = 0
  while prev_removed != removed:
    prev_removed = removed
    accessible = []
    for r in range(len(grid)):
      for c in range(len(grid[0])):
        if grid[r][c] == '@' and is_accessible(r, c):
          accessible.append((r, c))
          removed += 1
    remove_paper(accessible)
  return removed

# print("Part 1:", part1())
print("Part 2:", part2())