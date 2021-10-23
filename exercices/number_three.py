from random import randint, choice
from number_one import check_IPv4_address, check_IPv6_address


def generate_random_ipv4() -> str:
    def randint2() -> int:
        return randint(0, 255)
    ipv4 = f"{randint2()}.{randint2()}.{randint2()}.{randint2()}"
    if check_IPv4_address(ipv4):
        return ipv4
    raise ValueError("Random IPv4 generation failed, please try again.")

def generate_random_ipv4_in_range(start: str, end: str) -> str:
    if not check_IPv4_address(start):
        raise ValueError(f"{start} IPv4 is invalid.")
    elif not check_IPv4_address(end):
        raise ValueError(f"{end} IPv4 is invalid.")

    start, end = start.split("."), end.split(".")
    ipv4 = list()
    for i in range(4):
        try:
            start_i, end_i = int(start[i]), int(end[i])
        except ValueError as vex:
            print(f"{vex} : make sure you put integer inside your IPv4.")
        if start_i > end_i:
            raise ValueError(
                f"{start[i]} ({start}) is bigger than {end[i]} ({end}), start address is incorrect."
            )
        ipv4.append(
            str(randint(start_i, end_i))
        )
    return ".".join(ipv4)

def generate_random_ipv6() -> str:
    def randchar() -> str:
        # string.hexdigits --> return '0123456789abcdefABCDEF'
        return choice("0123456789abcdef")
    def randhex() -> str:
        return f"{randchar()}{randchar()}{randchar()}{randchar()}"
    ipv6 = f"{randhex()}:{randhex()}:{randhex()}:{randhex()}:{randhex()}:{randhex()}:{randhex()}:{randhex()}"
    if check_IPv6_address(ipv6):
        return ipv6
    raise ValueError("Random IPv6 generation failed, please try again.")

def main():
    print(generate_random_ipv4())
    print(
        generate_random_ipv4_in_range("192.168.1.45", "192.168.1.255")
    )
    print(generate_random_ipv6())

if __name__ == '__main__':
    main()