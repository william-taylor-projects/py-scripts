
# Documentation

Domain testing utility.

Usage:
    domain.py domain <domain> [--repeat=<times>] [--timeout=<secs>] [--headers=<show>] [--cookies=<show>]
    domain.py file <path> [--repeat=<times>] [--timeout=<secs>] [--headers=<show>] [--cookies=<show>]
    domain.py test [--repeat=<times>] [--timeout=<secs>] [--headers=<show>] [--cookies=<show>]
    domain.py -h | --help | -v | --version

Options:
  -h --help         Show this screen.
  -v --version      Show version.
  --repeat=<times>  How many times should we test the domain? [default: 1]
  --timeout=<secs>  Set the timeout for the http request (secs) [default: 1]
  --headers=<show>  Display response headers? [default: False]
  --cookies=<show>  Display response cookies? [default: False]

Dependencies:
    pip install docopt
    pip install requests
    pip install colorama

Examples:
    domain.py domain bing.com --repeat=5 --timeout=1
    domain.py file domains.txt --timeout=5
    domain.py bing.com > out.txt