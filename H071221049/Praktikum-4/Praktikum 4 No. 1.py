def mengurutkan(angka) :
    for i in range(len(angka)) :
        index_minimum = i
        for j in range(i+1, len(angka)) :
            if angka[index_minimum] > angka[j] :
                index_minimum = j
        if index_minimum != i :
            angka[i], angka[index_minimum] = angka[index_minimum], angka[i]


while True :
    angka = list(map(int, input('angka : ').split(' ')))
    mengurutkan(angka)
    print(f"Angka terurut {angka}")
    print(' ')
