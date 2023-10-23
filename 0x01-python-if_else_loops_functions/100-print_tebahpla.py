#!/usr/bin/python3
count = 0
for i in range(122, 96, -1):
    count += 1
    if count % 2 == 0:
        char = i - 32
    else:
        char = i
    print("{:c}".format(char), end="")
