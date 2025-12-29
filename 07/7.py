# Day 7: Laboratories

# read the input
with open('./input.txt', 'r') as f:
  lines = f.readlines()
  diagram = [line.strip() for line in lines]

def part1():
  splits = 0
  # beams track the position of beams in the current row being checked
  beams = [0] * len(diagram[0])
  beams[diagram[0].find('S')] = 1

  for row in diagram[2::2]:
    pos = -1
    while (pos := row.find('^', pos + 1)) != -1:
      if beams[pos]:
        splits += 1
        # update beam position after split
        beams[pos] = 0
        beams[pos-1] = 1
        beams[pos+1] = 1

  return splits

def part2():
  beams = [0] * len(diagram[0])
  beams[diagram[0].find('S')] = 1

  for row in diagram[2::2]:
    pos = -1
    while (pos := row.find('^', pos + 1)) != -1:
      if count := beams[pos]:
        beams[pos] = 0
        beams[pos-1] += count
        beams[pos+1] += count

  return sum(beams)

# print("Part 1:", part1())
print("Part 2:", part2())