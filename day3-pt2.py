#! /usr/bin/env python

from array import *

input = open("day3-input.txt", "r")
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

  # Enter shape into 2d array
  for x in range(int(edges[0]),int(size[0]) + int(edges[0])):
    for y in range(int(edges[1]),int(size[1]) + int(edges[1])):
      if (tilemap[x][y] == 0):
        tilemap[x][y] = 1
      else:
        tilemap[x][y] = 2

for line in lines:
  data = line.split(" ")
  edges = data[2][:-1].split(",")
  size = data[3][:-1].split("x")
  s = []
  # Check shape has consistent cut #s
  for x in range(int(edges[0]),int(size[0]) + int(edges[0])):
    for y in range(int(edges[1]),int(size[1]) + int(edges[1])):
      s.append(tilemap[x][y])

  if (s.count(s[0]) == len(s)):
    if (s[0] == 1):
      print(data[0][1:] + " " + str(s))
