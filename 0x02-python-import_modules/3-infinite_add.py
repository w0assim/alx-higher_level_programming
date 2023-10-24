#!/usr/bin/python3

if __name__ == "__main__":
    sum = 0
    if len(argv) <= 1:
        print("{}".format(sum))
    else:
        for i in range(1, len(argv)):
            sum += argv[i]
