# soal program 2
# cek inputan IP address

import re
x = int(input()) ; ip_lst = []

for i in range(x):
    string_ = input()
    ip_lst.append(string_)
def IP(c):
    if re.search(r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]?[0-9]).){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]?[0-9])$", c): 
        return "IPv4"
    elif re.search(r"^([\da-f]{1,4}:){7}([\da-f]{1,4}){1}$", c): 
        return "IPv6"
    else: 
        return "Bukan iP address"
for i in ip_lst:
    print(IP(i))