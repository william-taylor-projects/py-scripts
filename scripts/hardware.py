"""
Hardware descripter python program

Usage:
    

Options:
  

Dependencies:
   pip install python-hwinfo
   pip install wmi

Examples:
    
"""
from docopt import docopt
from wmi import WMI as WinInfo

def get_cpu_info():
    pass

def get_ram_info():
    pass

def get_os_info():
    pass

def get_gpu_info():
    pass

computer = WinInfo()

computer_info = computer.Win32_ComputerSystem()[0]
processor_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()[0]
os_info = computer.Win32_OperatingSystem()[0]


print(gpu_info)

"""
computer_info = computer.Win32_ComputerSystem()[0]
os_info = computer.Win32_OperatingSystem()[0]
proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()[0]

os_name = os_info.Name
os_version = ' '.join([os_info.Version, os_info.BuildNumber])
system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB

print('OS Name: {0}'.format(os_name))
print('OS Version: {0}'.format(os_version))
print('CPU: {0}'.format(proc_info.Name))
print('RAM: {0} GB'.format(system_ram))
print('Graphics Card: {0}'.format(gpu_info.Name))
"""