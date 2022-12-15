import re

    # 121.203.197.20
    # 2001:0db8:0000:0000:0000:ff00:0042:8329

    # 213.214.111.564
    # 444.444.444.444 not an ip address
    # 1050:0:0a:0:5:600:300c:326b

kondisi_ipv4 = r'(([0-1]?[\d][\d]?|2[0-4][\d]|25[0-5])\.){3}([0-1]?[\d][\d]?|2[0-4][\d]|25[0-5])$'
kondisi_ipv6 = r'(([\dA-Fa-f]{1,4}?\:){7})([\dA-Fa-f]{1,4})$'

n = int(input())
list = []

for i in range(n):
    s = input()
    list.append(s)

for j in list:
    ipv4 = re.search(kondisi_ipv4, j)
    ipv6 = re.search(kondisi_ipv6, j)
    if ipv4:
        print('IPv4')
    elif ipv6:
        print('IPv6')
    else:
        print('Bukan IP Address')