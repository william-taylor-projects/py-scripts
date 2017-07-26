
# Documentation

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
    linkedin.py ../templates/template.html image.png google.com > index.html
    linkedin.py custom.html image.png google.com > index.html