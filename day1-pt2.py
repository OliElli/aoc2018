#! /usr/bin/env python

input = open("day1-input.txt", "r")
# input = open("test-input.txt", "r")

lines = input.readlines()
total = 0
frequencies = {}

def apply_freq(lines, total, frequencies):
    count = 0
    while 1:
        count += 1
        print(count)
        for number in lines:
            total += int(number.rstrip())
            if total in frequencies.keys():
                print(total)
                return()
            frequencies[total] = 1

apply_freq(lines, total, frequencies)
