
# Documentation

BSc University Grade Viewer.

Usage:
    grades.py [--y1] [--y2] [--y3] [--y4] [--pause]
    grades.py -h | --help | -v | --version

Options:
    -h --help         Show this screen.
    -v --version      Show version.
    -p --pause        Pause between each graph
    --y1              Show year one
    --y2              Show year two
    --y3              Show year three
    --y4              Show year four

Dependencies:
   pip install matplotlib
   pip install docopt

Examples:
    grades.py --y3 --y4 --pause
    grades.py --y1 --y2