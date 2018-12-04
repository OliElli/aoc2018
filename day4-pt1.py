#! /usr/bin/env python

import re
pp = pprint.PrettyPrinter(indent=2)

input = open("day4-input.txt", "r")
lines = input.readlines()
lines = sorted(lines)   # sort it to make things easier

guard_id = ""
new_id = ""
sleeping = {}
sleeping_minutes = {}

for line in lines:
  date = line[6:11]
  time = line[12:17]
  
  m = re.search(r'Guard (#[0-9]+) begins shift', line)
  if m:
    guard_id = m.group(1)
    if not guard_id in sleeping.keys():
      sleeping[guard_id] = 0
    if not guard_id in sleeping_minutes.keys():
      sleeping_minutes[guard_id] = {}
      for x in range (0,59):
        sleeping_minutes[guard_id][x] = 0
  
  m = re.search(r'falls asleep', line)
  if m:
    start_time = int(time[3:5])

  m = re.search(r'wakes up', line)
  if m:
    end_time = int(time[3:5])
    total_time = end_time - start_time
    sleeping[guard_id] += total_time

    # Enter all sleeping minutes into dict
    for x in range (start_time, end_time):
      sleeping_minutes[guard_id][x] += 1

# Guard that sleeps the most:
sleepy_guard = max(sleeping, key=lambda key: sleeping[key])

print("Sleepy guard: " + sleepy_guard)
# Thanks internet:
s = [(k, sleeping_minutes[sleepy_guard][k]) for k in sorted(sleeping_minutes[sleepy_guard], key=sleeping_minutes[sleepy_guard].get, reverse=True)]
print("Sleepy minute: " + str(s[0][0]))
print("Product: " + str(int(sleepy_guard[1:])*s[0][0]))