# Day 6: Trash Compactor

import math

# read the input
with open('./input.txt', 'r') as f:
  lines = f.readlines()
  line1 = lines[0]
  line2 = lines[1]
  line3 = lines[2]
  line4 = lines[3]
  operations = lines[4]

def part1():
  grand_total = 0
  nums1 = [int(entry) for entry in line1.split()]
  nums2 = [int(entry) for entry in line2.split()]
  nums3 = [int(entry) for entry in line3.split()]
  nums4 = [int(entry) for entry in line4.split()]
  ops = operations.strip().split()
  for i in range(len(ops)):
    op = ops[i]
    num1, num2, num3, num4 = nums1[i], nums2[i], nums3[i], nums4[i]
    if op == '+':
      grand_total += num1 + num2 + num3 + num4
    elif op == '*':
      grand_total += num1 * num2 * num3 * num4
  return grand_total

def read_number(col):
  digit = 0
  num = 0
  if line4[col] != ' ':
    num += int(line4[col]) * 10**digit
    digit += 1
  if line3[col] != ' ':
    num += int(line3[col]) * 10**digit
    digit += 1
  if line2[col] != ' ':
    num += int(line2[col]) * 10**digit
    digit += 1
  if line1[col] != ' ':
    num += int(line1[col]) * 10**digit
  return num

def compute(nums, op):
  if op == '+':
    return sum(nums)
  elif op == '*':
    return math.prod(nums)
  return 0

def part2():
  grand_total = 0
  i = 0
  current_op = ''
  current_nums = []
  while i < len(line1)-1:
    if line1[i] == line2[i] == line3[i] == line4[i] == operations[i] == ' ':
      grand_total += compute(current_nums, current_op)
      current_nums = []
      current_op = ''
      i += 1
      continue
    if operations[i] == '+' or operations[i] == '*':
      current_op = operations[i]
    current_nums.append(read_number(i))
    i += 1
  grand_total += compute(current_nums, current_op)
  return grand_total

# print("Part 1:", part1())
print("Part 2:", part2())