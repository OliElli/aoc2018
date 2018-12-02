#! /usr/bin/env python

input = open("day1-input.txt", "r")
# input = open("test-input.txt", "r")

lines = input.readlines()
total = 0
frequencies = [0]

def apply_freq(lines, total, frequencies):
    count = 0
    while 1:
        count += 1
        print(count)
        for number in lines:
            total += int(number.rstrip())
            if total in frequencies:
                print(total)
                return()
            frequencies.append(total)

apply_freq(lines, total, frequencies)
