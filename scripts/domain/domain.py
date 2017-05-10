# Domain Script:
#   The following script should
#      a) Test domains are active and healthy
#      b) Print success error etc with color codes
#      c) use cli parsing lib

from colorama import init, Fore, Back, Style
from requests import get, status_codes

domains = [
    "http://www.williamsamtaylor.co.uk",
    "http://www.youngmoneyren.org",
    "http://www.should-throw-exception.com"
]

init()

print_success = lambda msg: print(Style.RESET_ALL + Fore.GREEN + msg)
print_warning = lambda msg: print(Style.RESET_ALL + Fore.YELLOW + msg)
print_error = lambda msg: print(Style.RESET_ALL + Fore.RED + msg)
print_info = lambda msg: print(Style.RESET_ALL + Fore.BLUE + msg)
print(Fore.CYAN + "Connecting to {0} domains...".format(len(domains)))

CODE, NAME = (0, 1)

def status_code(resp):
    name = status_codes._codes[resp.status_code][0]
    code = resp.status_code
    return (code, name.upper())

def headers(resp):
    header_text = ""
    for (name, value) in resp.headers.items():
        header_text += "\n  {0} = {1}".format(name, value)
    return header_text if len(header_text) else "None"

def cookies(resp):
    cookies_text = ""
    for (name, value) in resp.cookies.items():
        cookies_text += "\n  {0} = {1}".format(name, value)
    return cookies_text if len(cookies_text) else "None"


for domain in domains:
    print_info("Trying {0}".format(domain))
    response = None
    try:
        response = get(domain, timeout=1)
        status = status_code(response)

        if status[CODE] >= 200 and status[CODE] < 300:
            print_success("Code: {0} {1} ".format(*status))
        elif status[CODE] >= 300 and status[CODE] < 400:
            print_warning("Code: {0} {1} ".format(*status))
        else:
            print_error("Code: {0} {1} ".format(*status))

        print_success("Encoding: {0}".format(response.encoding))
        print_success("Headers: {0}".format(headers(response)))
        print_success("Cookies: {0}".format(cookies(response)))
    except Exception:
        print_error("Can't connect to {0}".format(domain))
        print_success("Skipping to next domain name")
