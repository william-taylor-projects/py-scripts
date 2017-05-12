"""
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
"""
from docopt import docopt
from wmi import WMI as WinInfo

def get_cpu_info(pc, cpu_info):
    print('CPU: {0}'.format(cpu_info.Name))

def get_ram_info(pc, os_info):
    print("RAM: {0}".format(float(os_info.TotalVisibleMemorySize) / 1048576.0)) 

def get_os_info(pc, os_info):
    print('OS Name: {0}'.format(os_name))
    print('OS Version: {0}'.format(os_version))

def get_gpu_info(pc, gpu_info):
    print('Graphics Card: {0}'.format(gpu_info.Name))

def main():
    config = docopt(__doc__, version='0.1')
    pc = WinInfo()

    processor_info = pc.Win32_Processor()[0]
    gpu_info = pc.Win32_VideoController()[0]
    os_info = pc.Win32_OperatingSystem()[0]
    pc_info = pc.Win32_ComputerSystem()[0]

    if config['--cpu']:
        get_cpu_info(pc, processor_info)
    if config['--gpu']:
        get_gpu_info(pc, gpu_info)
    if config['--ram']:
        get_ram_info(pc, os_info)
    if config['--os']:
        get_os_info(pc, os_info)

if __name__ == '__main__':
    main()