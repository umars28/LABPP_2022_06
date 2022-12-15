import re

def ipv4 (ip):
    pola1 = r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])"
    match1 = fr"{pola1}\.{pola1}\.{pola1}\.{pola1}"
    return re.fullmatch (match1, ip)

def ipv6 (ip) :
    pola1 = r"([0-9a-fA-F]{1,4})"
    match1 = fr"{pola1}:{pola1}:{pola1}:{pola1}:{pola1}:{pola1}:{pola1}:{pola1}"
    return re.fullmatch (match1, ip)

loop = int(input())
listIP = []
for a in range(loop):
    addressIP = input()
    listIP.append(addressIP)
for b in listIP:
    if ipv4 (b):
        print("IPv4")
    elif ipv6 (b):
        print("IPv6")
    else:
        print("Bukan IP Address")