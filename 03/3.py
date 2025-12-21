# Day 3: Lobby

# read the input
with open('./input.txt', 'r') as f:
  lines = f.readlines()
  banks = [entry.strip() for entry in lines]

def get_max_joltage(bank, digits):
  batteries = list(map(int, bank))
  place = digits - 1
  joltage = 0
  max_idx = 0
  while place >= 0:
    for i in range(max_idx, len(batteries)-place):
      if batteries[i] > batteries[max_idx]:
        max_idx = i
    joltage += batteries[max_idx] * (10 ** place)
    max_idx += 1
    place -= 1
  return joltage

def part1():
  total = 0
  for bank in banks:
    total += get_max_joltage(bank, 2)
  return total

def part2():
  total = 0
  for bank in banks:
    total += get_max_joltage(bank, 12)
  return total

# print("Part 1:", part1())
print("Part 2:", part2())