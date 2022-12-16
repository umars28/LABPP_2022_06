import re

kondisi = r'^[A-Za-z24680]{40}[103579\s]{5}$'

s = input()
hasil1 = re.findall(kondisi, s)
print(hasil1)
if len(s) == 45:
    if hasil1:
        print('true')
else:
    print('false')
