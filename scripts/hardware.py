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
    print('Threads: {0}'.format(cpu_info.ThreadCount))
    print('Cores: {0}'.format(cpu_info.NumberOfCores))
    print('Logical Processors: {0}'.format(cpu_info.NumberOfLogicalProcessors))
    print('Current Clock Speed: {0}'.format(cpu_info.CurrentClockSpeed))
    print('Max Clock Speed: {0}'.format(cpu_info.MaxClockSpeed))
    print('Voltage: {0}'.format(cpu_info.CurrentVoltage))
    print('L2 Cache: {0}'.format(cpu_info.L2CacheSize))
    print('L3 Cache: {0}'.format(cpu_info.L3CacheSize))
    print('Virtualization?: {0}'.format(cpu_info.VirtualizationFirmwareEnabled))

def get_ram_info(pc, os_info):
    print("Visiable Memory Size: {0}".format(os_info.TotalVisibleMemorySize))
    print("Virtual Memory Size: {0}".format(os_info.TotalVirtualMemorySize)) 
    print("Free Space In Paging Files: {0}".format(os_info.FreeSpaceInPagingFiles))
    print("Free Physical Memory: {0}".format(os_info.FreePhysicalMemory)) 
    print("Free Virtual Memory: {0}".format(os_info.FreeVirtualMemory)) 

def get_os_info(pc, os_info):
    print('OS Name: {0}'.format(os_info.Caption))
    print('OS Version: {0}'.format(os_info.Version))
    print('OS Architecture: {0}'.format(os_info.OSArchitecture))
    print('Windows Dir: {0}'.format(os_info.WindowsDirectory))
    print('Processes: {0}'.format(os_info.NumberOfProcesses))
    print('Users: {0}'.format(os_info.NumberOfUsers))

def get_gpu_info(pc, gpu_info):
    print('Graphics Card: {0}'.format(gpu_info.Name))
    print('Driver Version: {0}'.format(gpu_info.DriverVersion))
    print('Refresh Rate: {0}'.format(gpu_info.MaxRefreshRate))
    print('Description: {0}'.format(gpu_info.VideoModeDescription))
    print('Family: {0}'.format(gpu_info.VideoProcessor))

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