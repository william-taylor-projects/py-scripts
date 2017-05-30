"""
Cryptography utility for securing data

Usage:
    crypto.py <text>
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
from cryptography.fernet import Fernet
from docopt import docopt

def main():
    config = docopt(__doc__, version='0.1')

    key = Fernet.generate_key()
    txt = bytes(config['<text>'], 'utf-8')

    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(txt)

    print(key)
    print(cipher_text)

if __name__ == '__main__':
    main()