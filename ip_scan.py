import scapy.all as scapy
import sys
from termcolor import colored, cprint
text = colored('Authore:-Anubhab Mukherjee\n', 'red', attrs=['reverse', 'blink'])
print(text)
n=input("Enter your roter ip/cidr(Ex. 192.168.x.x/24): ")
scapy.arping(n)