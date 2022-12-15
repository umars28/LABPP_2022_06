import re

try:
    string_s=input('masukkan string s: ')
    if len(string_s)==45:
        sesuai = re.search("[A-Za-z2468]{40}[13579 ]{5}", string_s)
        if sesuai:
            print('true')
        else:
            print('false')
    else:
        print('false')
except:
    print('false')