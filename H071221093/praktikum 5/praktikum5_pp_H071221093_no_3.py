numbers1 = tuple(map(int, input('input angka-angka pertama:').split(' ')))
numbers2 = tuple(map(int, input('input angka-angka kedua:').split(' ')))
duplicate_numbers = []
no_duplicate = []

def del_duplicate(a_list) :
    for i in a_list :
        if i not in no_duplicate :
            no_duplicate.append(i)
    return no_duplicate

for i in numbers1 :
    for j in numbers2 :
        if i == j :
            duplicate_numbers.append(i)

del_duplicate(duplicate_numbers)


if len(no_duplicate) == 0 :
    print('tidak ada duplikat')
else:
    print(f'terdapat {len(no_duplicate)} angka duplikat, yaitu {tuple(no_duplicate)}')
