# Domain Script:
#   The following script should
#      a) Test domains are active and healthy
#      b) Print success error etc with color codes
#      c) use cli parsing lib

from requests import get
from colorama import init, Fore, Back, Style

init()

response = get("http://www.bing.com")

print(response.status_code)

print(Fore.GREEN + 'some red text')
print(Fore.YELLOW + 'some red text')
print(Fore.RED + 'some red text')
