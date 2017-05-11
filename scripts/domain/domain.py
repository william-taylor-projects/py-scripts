"""
Basic domain test cli utility.

Usage:
    domain.py <domain> [--repeat=<times>] [--timeout=<secs>] [--headers=<show>] [--cookies=<show>]
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
"""
from colorama import init as colorama, Fore, Back, Style
from urllib.parse import urlparse, ParseResult
from requests import get, status_codes
from docopt import docopt

print_success = lambda msg: print(Style.RESET_ALL + Fore.GREEN + msg)
print_warning = lambda msg: print(Style.RESET_ALL + Fore.YELLOW + msg)
print_error = lambda msg: print(Style.RESET_ALL + Fore.RED + msg)
print_info = lambda msg: print(Style.RESET_ALL + Fore.BLUE + msg)

def read_status_code(resp):
    name = status_codes._codes[resp.status_code][0]
    code = resp.status_code
    return (code, name.upper())

def read_headers(resp):
    header_text = ""
    for (name, value) in resp.headers.items():
        header_text += "\n  {0} = {1}".format(name, value)
    return header_text if len(header_text) else "None"

def read_cookies(resp):
    cookies_text = ""
    for (name, value) in resp.cookies.items():
        cookies_text += "\n  {0} = {1}".format(name, value)
    return cookies_text if len(cookies_text) else "None"

def fix_url(url, protocol = "http"):
    p = urlparse(url, protocol)
    netloc = p.netloc or p.path
    path = p.path if p.netloc else ''
    if not netloc.startswith('www.'):
        netloc = 'www.' + netloc
    p = ParseResult(protocol, netloc, path, *p[3:])
    return p.geturl()

def ping_domains(timeout, repeat, headers, cookies, domains):
    print(Fore.CYAN + "Connecting to {0} domains...".format(len(domains)))

    for domain in domains:
        for attempt in range(repeat):
            if repeat == 1:
                print_info("Trying {0}".format(domain))
            else:
                print_info("Trying {0}, Attempt #{1}".format(domain, attempt))
            try:
                response = get(domain, timeout=timeout)
                status = read_status_code(response)

                if status[0] >= 200 and status[0] < 300:
                    print_success("Code: {0} {1} ".format(*status))
                elif status[0] >= 300 and status[0] < 400:
                    print_warning("Code: {0} {1} ".format(*status))
                else:
                    print_error("Code: {0} {1} ".format(*status))

                print_success("Encoding: {0}".format(response.encoding))

                if headers:
                    print_success("Headers: {0}".format(read_headers(response)))
                if cookies:
                    print_success("Cookies: {0}".format(read_cookies(response)))
            except Exception:
                print_error("Can't connect to {0}".format(domain))
                print_success("Skipping to next {0}".format("domain" if repeat == 1 else "attempt"))

test_domains = [
    "williamsamtaylor.co.uk", 
    "github.com/william-taylor", 
    "youngmoneyren.org"
]

def main():
    arguments = docopt(__doc__, version='0.1')    
    headers = bool(arguments["--headers"])
    cookies = bool(arguments["--cookies"])
    timeout = int(arguments["--timeout"])
    repeat = int(arguments["--repeat"] )
    domains = []

    colorama()

    if arguments["<domain>"]:
        domains =  [fix_url(arguments["<domain>"])]
    elif arguments["test"]:
        domains = list(map(lambda x: fix_url(x), test_domains))
    elif arguments["<path>"]:
        with open(arguments["<path>"]) as file:
            for line in file.read().splitlines():
                domains.append(fix_url(line))
                
    ping_domains(timeout, repeat, headers, cookies, domains)

if __name__ == '__main__':
    main()