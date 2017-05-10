# Logical Operations

# Identity operator
a = 100
b = a

print (a is b) # ref comparison

# Comparison operators

print (a < b or b > a or a == b or a != b)

a = 5

print (0 <= a <= 10) # chaining

# Membership operator
c = [3, 6, 9]

print (6 in c)

# Logic operators

print (not 7 and 5 or 3) # ! && ||

def hello():
    print("Hello")

def nothing():
    print("")

# if statement
if 0:
    nothing()
elif 0:
    nothing()
else:
    hello()

# Single line if
print(20 if True else 10)

# While
while 0:
    nothing()
else:
    hello()

# For loop
for number in range(5):
    print(number)

# Exception
try:
    raise ValueError()
except Exception as err:
    print("Exception: ", err)
    pass
finally:
    nothing()

def sum_of_powers(*numbers, power=1):
    result = 0
    for num in numbers:
        result += num ** power
    return result

print(sum_of_powers(1, 2, 3))

add = lambda x, y: x + y

print(add(5, 5))

# disable with -O
assert 0 == 1