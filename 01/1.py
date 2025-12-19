# Day 1: Secret Entrance

# read the input
with open('./input.txt', 'r') as f:
  lines = f.readlines()
  lines = [entry.strip() for entry in lines]

DIAL_PTR = 50
DIAL_SIZE = 100

def part1():
  global DIAL_PTR
  password = 0
  for line in lines:
    direction, distance = line[0], int(line[1:]) % DIAL_SIZE

    if direction == 'L':
      DIAL_PTR = (DIAL_PTR - distance) % DIAL_SIZE
    elif direction == 'R':
      DIAL_PTR = (DIAL_PTR + distance) % DIAL_SIZE

    if DIAL_PTR == 0:
      password += 1

  return password

def part_2():
  global DIAL_PTR
  at_zero = 0
  
  for line in lines:
    direction, distance = line[0], int(line[1:])
    if distance > DIAL_SIZE:
      at_zero += distance // DIAL_SIZE
      distance %= DIAL_SIZE

    if direction == 'L':
      ptr = DIAL_PTR - distance
    elif direction == 'R':
      ptr = DIAL_PTR + distance
    if DIAL_PTR != 0 and (ptr < 0 or ptr > DIAL_SIZE):
      at_zero += 1
    DIAL_PTR = ptr % DIAL_SIZE

    if DIAL_PTR == 0:
      at_zero += 1

  return at_zero

# print("Part 1:", part1())
print("Part 2:", part_2())