
import collections
import copy
import math

# Tuples
emptyTuple = tuple()
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
emptyList = list()
list = [5, 5, 5, 5, 5]

first, *rest =  list

print(type(list))
print(first, rest)

# Set 
emptySet = set()
primeNumbers = { 2, 3, 5, 7, 11, 13 }

print(type(primeNumbers))

primeNumbers.clear()
primeNumbers.add(3)
primeNumbers.add(3)

print(primeNumbers)
print(type(frozenset({ 1, 2, 3 })))

# Dictionary
emptyDict = dict()
dict1 = {"key": "value"}
print(dict1)
dict1["key"] = 100
print(dict1)

for item in dict1.items():
    print(item[0], item[1])

for value in dict1.values():
    print(value)

defaultDict = collections.defaultdict(int)
defaultDict[0] += 5

print(defaultDict.values())

# Iterators
product = 1
i = iter([1, 2, 4, 8]) # __iter__
while True:
    try:
        product += next(i) # __next__
    except StopIteration: # Cant believe this
        break
print("{0} -> product".format(product))

# Copy

shallow = list[:]
shallowAgain = copy.copy(list)
deepcopy = copy.deepcopy(list)