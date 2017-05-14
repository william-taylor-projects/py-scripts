"""
Creates a redirect page for links on a LinkedIn profile page.

Usage:
    linkedin.py <template> <image> <link> [--redirect=<v>]
    linkedin.py -h | --help | -v | --version
    
Options:
  -h --help          Show this screen.
  -v --version       Show version.
  -r --redirect=<v>  Should the page redirect. [default: False]

Dependencies:
   pip install docopt

Examples:
    linkedin.py ../data/template.html image.png google.com > index.html
    linkedin.py custom.html image.png google.com > index.html
"""
from urllib.parse import urlparse, ParseResult
from docopt import docopt

tokens = [ ('{','{{'), ('}', '}}'),  ('_Z', '{0}'), ('_O', '{1}'), ('_T', '{2}') ]

def fix_url(url, protocol = "http"):
    p = urlparse(url, protocol)
    netloc = p.netloc or p.path
    path = p.path if p.netloc else ''
    if not netloc.startswith('www.'):
        netloc = 'www.' + netloc
    p = ParseResult(protocol, netloc, path, *p[3:])
    return p.geturl()

def main():
    config = docopt(__doc__, version='0.1')
    redirct = config["--redirect"]
    image = config["<image>"]
    link = config["<link>"]

    with open(config['<template>']) as file:
        template = file.read().replace('\n', '')
        for (key, value) in tokens:
            template = template.replace(key, value)
        print(template.format(image, redirct.lower(), fix_url(link)))

if __name__ == '__main__':
    main()
