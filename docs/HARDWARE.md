
# Documentation

Hardware descripter python program

Usage:
    hardware.py [--cpu] [--gpu] [--ram] [--os]
    hardware.py -h | --help | -v | --version

Options:
    -c --cpu          Show CPU info
    -g --gpu          Show GPU info
    -r --ram          Show RAM info
    -o --os           Show OS info
    -h --help         Show this screen.
    -v --version      Show version.

Dependencies:
   pip install docopt
   pip install wmi

Examples:
    hardware.py --gpu > gpu_info.txt
    hardware.py --cpu