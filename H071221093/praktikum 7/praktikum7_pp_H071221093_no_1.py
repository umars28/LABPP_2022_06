import re

s = input('')
# print(len(s))

first_regex = r'[02468_]'
sec_regex = r'[13579 ]'

resultone = re.findall(sec_regex, s[0:40])
resultwo = re.findall(first_regex, s[40:45])

if resultone or resultwo:
    print('\nfalse')
elif len(s)<45 or len(s)>45:
    print('\nfalse')
else:
    print('\ntrue')
    