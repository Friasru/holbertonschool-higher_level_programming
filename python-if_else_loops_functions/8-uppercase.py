#!/usr/bin/python3
def uppercase(str):
    for c in str:
        ascii_val = ord(c) - 32 if ord(c) >= 97 and ord(c) <= 122 else ord(c)
        print("{:c}".format(ascii_val), end="")
    print()
