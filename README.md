'''
The following python script can be run on either a Windows or Unix based system.
This script returns simple basic host and network information and then clears the system logs.
'''

import platform # type: ignore
import os
import socket # type: ignore
import getpass # type: ignore

print("\033[32mHost Infomation \033[0m")
print(f"OS Infomation: {platform.system()} {platform.release()}, Version {platform.version()}")
print(f"CPU Information: {platform.processor()} {platform.machine()}")
print(f"Host Name: {platform.node()}")
print(f"Host Name: {getpass.getuser()}")
print("\n\033[32mNetwork Infomation \033[0m")
print(f"IPv4 Address: {socket.gethostbyname(platform.node())}")
print("DNS Information:")
if platform.system() == "Windows":
    print(os.system("ipconfig /displaydns"))
else:
    print(os.system("ip a"))

# Clearing the Logs
if platform.system() == "Windows":
    print(os.system("wevtutil cl System"))
    print(os.system("wevtutil cl Security"))
else:
    print(os.system("> /var/log/auth.log"))
