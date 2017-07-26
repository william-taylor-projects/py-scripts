
# Documentation

Benchmark response time on a domain

Usage:
    response.py <domain> [--times=<count>]
    response.py -h | --help | -v | --version

Options:
    -t --times=<count>   Hits to average. [default:10]
    -h --help         Show this screen.
    -v --version      Show version.

Dependencies:
   pip install requests
   pip install docopt

Example:
    response.py bing.com --times=10 > times.txt
    response.py bing.com