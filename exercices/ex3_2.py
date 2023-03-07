import mymodip.ipv4 as spip4

def main():
#   try:
#     bla=spip4.generate_random_ipv4()
#     print(f"ceci est une ip {bla}")
#   except ValueError:
#       return "not correct"

    ip1="192.168.1.10"
    ip2="200.168.1.90"
    try:
        bla=spip4.generate_random_ipv4_range(ip1,ip2)
    except ValueError:
        return "not correct"
    bla=spip4.generate_random_ipv4_range(ip1,ip2)
    print(bla)
if __name__ == "__main__":
  main()
