import sys

Zero = [
    "  ***  ",
    " *   * ",
    "*     *",
    "*     *",
    "*     *",
    " *   * ",
    "  ***  "
]

One = [
    "   *   ",
    " * *   ",
    "*  *   ",
    "   *   ",
    "   *   ",
    "   *   ",
    " ***** "
]

Two = [
    "   *   ",
    " *   * ",
    "*    * ",
    "   *   ",
    " *     ",
    " *     ",
    " ***** " 
]

Three = [
    " * * * ",
    "     * ",
    "     * ",
    " * * * ",
    "     * ",
    "     * ",
    " * * * " 
]

Four = [
    " *   * ",
    " *   * ",
    " *   * ",
    " * * * ",
    "     * ",
    "     * ",
    "     * " 
]

Five = [
    " * * * ",
    " *     ",
    " *     ",
    " * * * ",
    "     * ",
    "     * ",
    " * * * " 
]

Six = [
    " * * * ",
    " *     ",
    " *     ",
    " * * * ",
    " *   * ",
    " *   * ",
    " * * * " 
]

Seven = [
    " * * * ",
    "     * ",
    "     * ",
    "     * ",
    "     * ",
    "     * ",
    "     * " 
]

Eight = [
    " * * * ",
    " *   * ",
    " *   * ",
    " * * * ",
    " *   * ",
    " *   * ",
    " * * * " 
]

Nine = [
    " * * * ",
    " *   * ",
    " *   * ",
    " * * * ",
    "     * ",
    "     * ",
    " * * * " 
]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    digits = sys.argv[1]
    row = 0
    while row < len(Zero):
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            digit[row] = digit[row].replace("*", str(number))
            line += digit[row] + " "
            column += 1
        print(line)
        row += 1
except IndexError:
    print('usage: bit-digits.py <number>')
except ValueError as err:
    print(err, "in", digits)