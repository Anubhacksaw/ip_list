import scapy.all as scapy
import sys
from termcolor import colored, cprint
cprint('Authore:-Anubhab Mukherjee\n', 'red', attrs=['reverse', 'blink'])
n=input("Enter your default gateway/cidr(Ex. 192.168.x.x/24): ")
scapy.arping(n)
cprint('\n https://github.com/Anubhab-ai\n', 'yellow')
