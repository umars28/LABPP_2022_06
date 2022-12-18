#program soal 1
# cek string

import re
x = input()

if re.search(r"^[24680a-zA-Z]{40}[13579\s]{5}$", x):
    print(True)
else:
    print(False)