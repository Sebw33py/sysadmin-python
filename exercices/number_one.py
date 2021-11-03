import re
from typing import List

CENSORED = "{CENSORED}"

def regex_replace_words_from_text(text: str, words: List[str]) -> str:
    regex = re.compile("|".join(words))
    return re.sub(
        regex, CENSORED, text
    )

def replace_words_from_text(text: str, words: List[str]) -> str:
    for word in words:
        text = text.replace(word, CENSORED)
    return text

def ask_for_ipv4() -> str:
    ipv4 = input("Entrez une adresse IPv4 respectant le format: xxx.xxx.xxx.xxx\n")
    if check_IPv4_address(ipv4):
        print("Votre adresse IPv4 est valide !")
        return ipv4
    else:
        print("Votre adresse IPv4 est incorrect !")
        return ""

def check_IPv4_address(ip: str) -> bool:
    try:
        for i in ip.split('.'):
            if not 0 <= int(i) <= 255:
                return False
    except ValueError:
        # Error in the IPv4 !
        return False
    return True

def check_IPv6_address(ip: str) -> bool:
    try:
        for i in ip.split(':'):
            if not 0x0000 <= int(i, 16) <= 0xFFFF:
                return False
    except ValueError:
        # Error in the IPv6 !
        return False
    return True

def check_IPv4_address_and_mask(ip: str, mask: str) -> bool:
    if not check_IPv4_address(ip) or not check_IPv4_address(mask):
        return False
    return True

def check_IPv6_address_and_prefix(ip: str, prefix: str) -> bool:
    if not check_IPv6_address(ip):
        return False
    # Remove '/' if any
    prefix = prefix.replace("/", "")
    try:
        if not 1 <= int(prefix) <= 128:
            return False
    except ValueError:
        return False
    return True

def main():
    ipv4 = ask_for_ipv4()
    print(check_IPv4_address("192.168.1.45"))
    print(check_IPv4_address("192.168.1111.45"))
    print(check_IPv6_address("2001:0db8:3456:1234:fffa:8a2e:0370:7334"))
    print(check_IPv6_address("2001:0db8:3456:1234:fgff:8a2e:0370:7334"))
    print(check_IPv4_address_and_mask("192.168.1.45", "255.255.0.0"))
    print(check_IPv4_address_and_mask("192.168.1.45", "255.255.2555.0"))
    print(check_IPv6_address_and_prefix("2001:0db8:3456:1234:fffa:8a2e:0370:7334", "64"))
    print(check_IPv6_address_and_prefix("2001:0db8:3456:1234:fffa:8a2e:0370:7334", "132"))

    # Text has been generated with: https://app.inferkit.com/demo
    text: str = ""
    with open("./statics/text.txt", "r") as f:
        text = f.read()
    regex_replace_words_from_text(text, ["couldn", "was", "like"])
    replace_words_from_text(text, ["couldn", "was", "like"])

if __name__ == '__main__':
    main()