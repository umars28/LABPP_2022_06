array_1 = list(map(int, input('Input array ke 1 : ').split()))
# x = set(int(i) for i in array_1)
array_2 = list(map(int, input('Input array ke 2 : ').split()))
# y = set(int(i) for i in array_2)
array_3 = array_1 + array_2
duplicate_item = []
for i in array_1 :
    if array_3.count(i) > 1 :
        if i not in duplicate_item :
            duplicate_item.append(i)

if len(duplicate_item) == 0 :
    print('Tidak ada yang terduplikat')
else :
    a = len(duplicate_item)

print('Terdapat {} buah duplikat yaitu {}'. format(a, tuple(duplicate_item)))