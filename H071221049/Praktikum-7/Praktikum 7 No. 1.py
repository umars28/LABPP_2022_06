import re

str = input("Masukkan string : ")
string_s = r'^(((0|2|4|6|8)|[a-z,A-Z]){40})+((1|3|5|7|9| ){5})$'

result = re.match(string_s,str)

if result :
    print("true")
else :
    print("false")