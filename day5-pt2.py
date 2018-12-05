#! /usr/bin/env python

import re
from string import ascii_lowercase

input = open("day5-input.txt", "r")
lines = input.readlines()

options = {}
results = {}

for i in ascii_lowercase:
  options[i] = re.sub("(?i)["+i+"]", "", lines[0])

def find_dupes(line): 
  i = 0
  char = ""
  # output = ""
  dupe = 0
  positions = []
  for x in line:
    if dupe == 1:
      dupe = 0
      continue
    if char.lower() == x.lower():
      if (char.islower() and x.isupper()) or (char.isupper() and x.islower()):
        positions.append(i)
        if i < len(line) - 1:
          char = line[i+1]
        else:
          char = x
        i += 2
        dupe = 1
        continue
    char = x
    i += 1

  # Remove the duplicates in one go
  j = 0
  for i in positions:
    line = str(line[:i-1-j] + line[i+1-j:])
    j += 2

  return(line)

for j in options:
  print("Attempt " + j)
  string = options[j]
  while True:
    string_before = string
    string = find_dupes(string)
    if len(string_before) == len(string):
      break
  results[j] = len(string)

# Order the results to get the smallest at the beginning of the array
s = [(k, results[k]) for k in sorted(results, key=results.get)]

print(s[0][1])
