#! /usr/bin/env python

import re
import sys

sys.setrecursionlimit(150000)

input = open("day5-input.txt", "r")
lines = input.readlines()

def find_dupes(line): 
  i = 0
  char = ""
  output = ""
  for x in line:
    string = line
    if char.lower() == x.lower():
      if (char.islower() and x.isupper()) or (char.isupper() and x.islower()):
        output = str(string[:i-1] + string[i+1:])
        string = find_dupes(output)
        return(string)
    char = x
    i += 1
  return(string)

result = find_dupes(lines[0])
print(result)