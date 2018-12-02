#! /usr/bin/env python

input = open("day1-input.txt", "r")
lines = input.readlines()
total = 0
for number in lines:
  total += int(number.rstrip())
print(total)
