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

def fix_url(url, protocol = "http"):
    p = urlparse(url, protocol)
    netloc = p.netloc or p.path
    path = p.path if p.netloc else ''
    if not netloc.startswith('www.'):
        netloc = 'www.' + netloc
    p = ParseResult(protocol, netloc, path, *p[3:])
    return p.geturl()

def main(html):
    config = docopt(__doc__, version='0.1')

    redirct = config["--redirect"]
    image = config["<image>"]
    link = config["<link>"]
    
    print(html.format(image, redirct.lower(), fix_url(link)))

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Enter title...</title>

    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Enter description...">
    <meta name="author" content="william taylor">
    <meta charset="utf-8">

    <style type="text/css">
        * {{ margin: 0px; padding: 0px; }}
        
        .sk-circle {{
            margin: 40px auto;
            width: 40px;
            height: 40px;
            position: relative;
        }}
        
        .sk-circle .sk-child {{
            width: 100%;
            height: 100%;
            position: absolute;
            left: 0;
            top: 0;
        }}
        
        .sk-circle .sk-child:before {{
            content: '';
            display: block;
            margin: 0 auto;
            width: 15%;
            height: 15%;
            background-color: #333;
            border-radius: 100%;
            -webkit-animation: sk-circleBounceDelay 1.2s infinite ease-in-out both;
            animation: sk-circleBounceDelay 1.2s infinite ease-in-out both;
        }}
        
        .sk-circle .sk-circle2 {{
            -webkit-transform: rotate(30deg);
            -ms-transform: rotate(30deg);
            transform: rotate(30deg);
        }}
        
        .sk-circle .sk-circle3 {{
            -webkit-transform: rotate(60deg);
            -ms-transform: rotate(60deg);
            transform: rotate(60deg);
        }}
        
        .sk-circle .sk-circle4 {{
            -webkit-transform: rotate(90deg);
            -ms-transform: rotate(90deg);
            transform: rotate(90deg);
        }}
        
        .sk-circle .sk-circle5 {{
            -webkit-transform: rotate(120deg);
            -ms-transform: rotate(120deg);
            transform: rotate(120deg);
        }}
        
        .sk-circle .sk-circle6 {{
            -webkit-transform: rotate(150deg);
            -ms-transform: rotate(150deg);
            transform: rotate(150deg);
        }}
        
        .sk-circle .sk-circle7 {{
            -webkit-transform: rotate(180deg);
            -ms-transform: rotate(180deg);
            transform: rotate(180deg);
        }}
        
        .sk-circle .sk-circle8 {{
            -webkit-transform: rotate(210deg);
            -ms-transform: rotate(210deg);
            transform: rotate(210deg);
        }}
        
        .sk-circle .sk-circle9 {{
            -webkit-transform: rotate(240deg);
            -ms-transform: rotate(240deg);
            transform: rotate(240deg);
        }}
        
        .sk-circle .sk-circle10 {{
            -webkit-transform: rotate(270deg);
            -ms-transform: rotate(270deg);
            transform: rotate(270deg);
        }}
        
        .sk-circle .sk-circle11 {{
            -webkit-transform: rotate(300deg);
            -ms-transform: rotate(300deg);
            transform: rotate(300deg);
        }}
        
        .sk-circle .sk-circle12 {{
            -webkit-transform: rotate(330deg);
            -ms-transform: rotate(330deg);
            transform: rotate(330deg);
        }}
        
        .sk-circle .sk-circle2:before {{
            -webkit-animation-delay: -1.1s;
            animation-delay: -1.1s;
        }}
        
        .sk-circle .sk-circle3:before {{
            -webkit-animation-delay: -1s;
            animation-delay: -1s;
        }}
        
        .sk-circle .sk-circle4:before {{
            -webkit-animation-delay: -0.9s;
            animation-delay: -0.9s;
        }}
        
        .sk-circle .sk-circle5:before {{
            -webkit-animation-delay: -0.8s;
            animation-delay: -0.8s;
        }}
        
        .sk-circle .sk-circle6:before {{
            -webkit-animation-delay: -0.7s;
            animation-delay: -0.7s;
        }}
        
        .sk-circle .sk-circle7:before {{
            -webkit-animation-delay: -0.6s;
            animation-delay: -0.6s;
        }}
        
        .sk-circle .sk-circle8:before {{
            -webkit-animation-delay: -0.5s;
            animation-delay: -0.5s;
        }}
        
        .sk-circle .sk-circle9:before {{
            -webkit-animation-delay: -0.4s;
            animation-delay: -0.4s;
        }}
        
        .sk-circle .sk-circle10:before {{
            -webkit-animation-delay: -0.3s;
            animation-delay: -0.3s;
        }}
        
        .sk-circle .sk-circle11:before {{
            -webkit-animation-delay: -0.2s;
            animation-delay: -0.2s;
        }}
        
        .sk-circle .sk-circle12:before {{
            -webkit-animation-delay: -0.1s;
            animation-delay: -0.1s;
        }}
        
        @-webkit-keyframes sk-circleBounceDelay {{
            0%, 80%, 100% {{
                -webkit-transform: scale(0);
                transform: scale(0);
            }}
            40% {{
                -webkit-transform: scale(1);
                transform: scale(1);
            }}
        }}
        
        @keyframes sk-circleBounceDelay {{
            0%, 80%, 100% {{
                -webkit-transform: scale(0);
                transform: scale(0);
            }}
            40% {{
                -webkit-transform: scale(1);
                transform: scale(1);
            }}
        }}
        
        .center {{
            margin: auto;
            position: absolute;
            top: 0;
            left: 0;
            bottom: 0;
            right: 0;
        }}
    </style>
</head>
<body>
    <div class="sk-circle center">
        <div class="sk-circle1 sk-child"></div>
        <div class="sk-circle2 sk-child"></div>
        <div class="sk-circle3 sk-child"></div>
        <div class="sk-circle4 sk-child"></div>
        <div class="sk-circle5 sk-child"></div>
        <div class="sk-circle6 sk-child"></div>
        <div class="sk-circle7 sk-child"></div>
        <div class="sk-circle8 sk-child"></div>
        <div class="sk-circle9 sk-child"></div>
        <div class="sk-circle10 sk-child"></div>
        <div class="sk-circle11 sk-child"></div>
        <div class="sk-circle12 sk-child"></div>
    </div>
    <img style='display:none;' src='{0}' />
    <script>
        if ({1}) {{ window.location = '{2}' }}
    </script>
</body>
</html>
"""

if __name__ == '__main__':
    main(html)
