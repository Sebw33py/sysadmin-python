import ipaddress

def check_ip_adress(a):
  try:
    return ipaddress.ip_address(a)
  except ValueError:
    return "not correct"

def is_ipv4_mask(octet):
    octets = octet.split(".")
    return len(octets) == 4 and \
           all(o.isdigit() and 0 <= int(o) < 256 for o in octets)

def main():
  IP=input("Enter your IP: ")
  MASK=input("Enter your MASK: ")
  print(f"The IP is", IP)
  print(f"The MASK is", MASK)
  print(f"the IP is",check_ip_adress(IP))
  print(f"the MASK validity is ",is_ipv4_mask(MASK))

if __name__ == "__main__":
  main()  