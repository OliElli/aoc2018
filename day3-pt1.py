#! /usr/bin/env python

from array import *

input = open("day3-input.txt", "r")
# input = open("test-input.txt", "r")
lines = input.readlines()

tilemap = []
count = 0

# Initialise 1000 x 1000 array of zeroes
for i in range (0, 1000):
  new = []
  for j in range (0, 1000):
    new.append(0)
  tilemap.append(new)

for line in lines:
  data = line.split(" ")
  edges = data[2][:-1].split(",")
  size = data[3][:-1].split("x")

  # data
  shape_id = data[0]
  left_edge = edges[0]
  top_edge = edges[1]
  width = size[0]
  height = size[1]

  # Enter shape into 2d array
  for x in range(int(left_edge),int(width) + int(left_edge)):
    for y in range(int(top_edge),int(height) + int(top_edge)):
      tilemap[x][y] += 1

for row in tilemap:
  for val in row:
    if val > 1:
      count += 1
print("Overlaps: " + str(count))
