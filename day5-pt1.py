#! /usr/bin/env python

import re

input = open("test-input.txt", "r")
lines = input.readlines()

print(lines[0])

def find_dupes(line): 
  i = 0
  char = ""
  print(line)
  for x in line:
    string = line
    if char.lower() == x.lower():
      if (char.islower() and x.isupper()) or (char.isupper() and x.islower()):
        output = str(string[:i-1] + string[i+1:])
        # print(output + " " + str(i))
        find_dupes(output)
    char = x
    i += 1
  return(string)

result = find_dupes(lines[0])

print(result)