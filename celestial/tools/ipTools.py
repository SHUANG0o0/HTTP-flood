
import sys
import socket
import ipaddress
import requests
from urllib.parse import urlparse

from time import sleep
from colorama import Fore



def __isCloudFlare(link):
    parsed_uri = urlparse(link)
    domain = "{uri.netloc}".format(uri=parsed_uri)
    try:
        origin = socket.gethostbyname(domain)
        iprange = requests.get("https://www.cloudflare.com/ips-v4").text
        ipv4 = [row.rstrip() for row in iprange.splitlines()]
        for i in range(len(ipv4)):
            if ipaddress.ip_address(origin) in ipaddress.ip_network(ipv4[i]):
                print(
                    f"{Fore.RED}[!] {Fore.CYAN}此目标受cloud云防护,攻击可能不会有太大效果"
                )
                sleep(1)
    except socket.gaierror:
        return False




def __GetAddressInfo(target):
    try:
        ip = target.split(":")[0]
        port = int(target.split(":")[1])
    except IndexError:
        print(f"{Fore.RED}[!] {Fore.MAGENTA}未设置端口{Fore.RESET}")
        sys.exit(1)
    else:
        return ip, port




def __GetURLInfo(target):
    if not target.startswith("http"):
        target = f"http://{target}"
    return target


def GetTargetAddress(target, method):
    url = __GetURLInfo(target)
    __isCloudFlare(url)
    return url



def InternetConnectionCheck():
    try:
        requests.get("https://baidu.com", timeout=10)
    except:
        print(
            f"{Fore.RED}[!] {Fore.MAGENTA}你没有连接互联网"
        )
        sys.exit(1)
