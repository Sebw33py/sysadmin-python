import socket
import struct
import random
import ipaddress

def check_ip_adress(a):
  try:
    return ipaddress.ip_address(a)
  except ValueError:
    return "not correct"

def generateipv4():
    ip_generated=socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    print(ip_generated)


# ip = ".".join(map(str, (random.randint(0, 255) 
#                         for _ in range(4))))


# ip = '{}.{}.{}.{}'.format(*random.sample(range(0,255),4))

# def generate_random_ipv4() -> str:
#     def randint2() -> int:
#         return random.randint(0, 255)
#     ipv4 = f"{randint2()}.{randint2()}.{randint2()}.{randint2()}"
#     return ipv4


def generate_random_ipv4_range(start,end) -> str:
    
    start = start.split(".")
    end = end.split(".")
    ipv4 = []
    for i in range(4):
        start_i=int(start[i])
        end_i=int(end[i])
        ipv4.append(
            str(random.randint(start_i,end_i))     
        )
        return ".".join(ipv4)