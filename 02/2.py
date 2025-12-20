# Day 2: Gift Shop

# read the input
with open('./input.txt', 'r') as f:
  lines = f.readline().strip().split(',')

def is_invalid(id):
  if len(id) % 2 != 0: return False
  half = len(id) // 2
  return id[:half] == id[half:]

def part1():
  solution = 0
  for id_range in lines:
    start, end = map(int, id_range.split('-'))
    for id in range(start, end + 1):
      if is_invalid(str(id)):
        solution += id
  return solution

def is_repeated_seq(id, seq):
  if len(id) % len(seq) != 0:
    return False
  head = len(seq)
  while head < len(id):
    if id[head:head+len(seq)] != seq:
      return False
    head += len(seq)
  return True

def is_invalid_2(id):
  if len(id) <= 1: return False
  for tail in range(1, len(id)):
    sequence = id[:tail]
    if is_repeated_seq(id, sequence):
      return True
  return False

def part2():
  solution = 0
  for id_range in lines:
    start, end = map(int, id_range.split('-'))
    for id in range(start, end + 1):
      if is_invalid_2(str(id)):
        solution += id
  return solution

# print(part1())
print(part2())