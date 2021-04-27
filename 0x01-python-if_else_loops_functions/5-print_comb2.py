#!/usr/bin/python3
charend = ", "
for i in range(0, 100):
    if i < 1:
        print("{}{}".format(0, i), end=charend)
    else:
        if i == 99:
            charend = "\n"
        print(i, end=charend)
