#! /usr/bin/env python

input = open("day2-input.txt", "r")
# input = open("test-input.txt", "r")
lines = input.readlines()
i = 0

for line in lines:
  line = line.rstrip()
  i += 1
  for line2 in lines[i:]:
    output = ""
    match = 0
    letter_num = 0
    for letter in line:
      if letter == line2[letter_num]:
        match += 1
        output += letter
      letter_num += 1
    if len(line) - match == 1:
      print(line)
      print(line2)
      print("Output: " + output)
