
import sys
import random

def get_int(msg, min, default):
    while True:
        try:
            line = input(msg)
            if not line and default is not None:
                return default
            i = int(line)
            if i < min:
                print("music be >=", min)
            else:
                return i
        except ValueError as err:
            print(err)

rows = get_int("rows: ", 1, None)
cols = get_int("cols: ", 1, None)
min = get_int("min: ", -100000, 0)

default = 1000
if default < min:
    default = 2 * min
max = get_int("max: ", min, default)
row = 0

while row < rows:
    line = ""
    column = 0
    while column < cols:
        i = random.randint(min, max)
        s = str(i)
        while len(s) < 10:
            s = " " + s
        line += s
        column += 1
    print(line)
    row += 1