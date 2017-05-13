"""
Benchmark response time on a domain

Usage:
    response.py <domain> [--times=<count>]
    response.py -h | --help | -v | --version

Options:
    -t --times=<count>   Hits to average. [default:10]
    -h --help         Show this screen.
    -v --version      Show version.

Dependencies:
   pip install docopt

"""
from urllib.parse import urlparse, ParseResult
from requests import get
from docopt import docopt

def fix_url(url, protocol = "http"):
    p = urlparse(url, protocol)
    netloc = p.netloc or p.path
    path = p.path if p.netloc else ''
    if not netloc.startswith('www.'):
        netloc = 'www.' + netloc
    p = ParseResult(protocol, netloc, path, *p[3:])
    return p.geturl()

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def benchmark_domain(domain, times):
    recorded_times = []
    for num in range(times):
        response = get(domain)
        secs = response.elapsed.total_seconds()
        recorded_times.append(secs)
    return (mean(recorded_times), recorded_times)

def print_times(result_pair):
    print('Average: {0:0.2f} secs'.format(result_pair[0]))
    print('Times: ')

    for time in result_pair[1]:
        print('  {0:0.2f} secs'.format(time))

def main():
    config = docopt(__doc__, version='0.1')
    domain = fix_url(config['<domain>'])
    times = benchmark_domain(domain, int(config['--times'] or 5))
    print_times(times)

if __name__ == '__main__':
    main()
