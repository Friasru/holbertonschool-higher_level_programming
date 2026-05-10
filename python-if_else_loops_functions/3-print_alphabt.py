#!/usr/bin/python3
for i in range(26):
    if i != 4 and i != 16:
        print("{:c}".format(ord('a') + i), end="")
