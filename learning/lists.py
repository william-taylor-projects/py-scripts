
import collections
import math

# Tuples
other = ("ginger", "orange")
hair = ("black", "brown", "blonde", "red")
a, b = (1, 2)

print(hair[2])
print(hair + other)
print(a, b)

del a, b

FIRST, LAST = (0, 4)
numbers = (0, 1, 2, 3, 4)

print(numbers[FIRST], numbers[LAST])

for x, y in ((1, 1), (2, 2)):
    print(math.hypot(x, y))

Point = collections.namedtuple("Point", "x y z")
points = []
points.append(Point(25, 45, 60))
points.append(Point(20, 30, 20))
points.append(Point(10, 45, 30))
print(points)

# Lists

list = [5, 5, 5, 5, 5]

first, *rest =  list

print(first, rest)

# Set 