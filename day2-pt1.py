#! /usr/bin/env python

input = open("day2-input.txt", "r")
# input = open("test-input.txt", "r")
lines = input.readlines()

twice = 0
thrice = 0

for line in lines:
  line = line.rstrip()
  count = {}
  inside_twice = 0
  inside_thrice = 0

  for letter in line:
    if letter not in count:
      count[letter] = 1
    else:
      count[letter] += 1
  for result in count:
    if count[result] == 2:
      inside_twice = 1
    elif count[result] == 3:
      inside_thrice = 1
  twice = twice + inside_twice
  thrice = thrice + inside_thrice

total = twice*thrice
print("checksum: " + str(total))
