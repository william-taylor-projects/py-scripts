"""
Cryptography utility for securing data

Usage:
    crypto.py <key> <text>
    crypto.py -h | --help | -v | --version

Dependencies:
    pip install cryptography
    pip install docopt

Options:
  -h --help         Show this screen.
  -v --version      Show version.

Examples:
    crypto.py helloworld
"""
from docopt import docopt
from pyaes import *

import string
import random

# We need a random initialization vector of 16 bytes
init_vector = random.choice(string.ascii_letters) * 16

def main(config):
    entered_key = config["<key>"]

    if len(entered_key) is not 32:
        print("Key must be 32 bytes...")
    else:
        aes = AESModeOfOperationCBC(entered_key, iv = init_vector.encode())
        txt = aes.encrypt(config["<text>"])

        print(repr(txt))


if __name__ == '__main__':
    main(docopt(__doc__, version='0.1'))