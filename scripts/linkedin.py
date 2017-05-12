"""
Creates a redirect page for links on a LinkedIn profile page.

Usage:
    linkedin.py <image> <link> [--redirect=<v>]
    linkedin.py -h | --help | -v | --version
    
Options:
  -h --help          Show this screen.
  -v --version       Show version.
  -r --redirect=<v>  Should the page redirect. [default: False]
  
Dependencies:
   pip install docopt

Example:
    linkedin.py image.png google.com > index.html
"""
from urllib.parse import urlparse, ParseResult
from docopt import docopt

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Linkedin</title>

    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="linkedin redirect page">
    <meta name="author" content="william taylor">
    <meta charset="utf-8">
</head>
<body>
   <img src='{0}' />
   <script>
        if({1})
            window.location = '{2}';
   </script>
</body>
</html>
"""

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
    
    print(html.format(image, redirct.lower(), fix_url(link)))

if __name__ == '__main__':
    main()
