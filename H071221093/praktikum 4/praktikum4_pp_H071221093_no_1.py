import numbers


def sorting(numbers) :
    for i in range(len(numbers)) :
        index_minimum = i
        for j in range(i+1, len(numbers)) :
            print(j)
            if numbers[index_minimum] > numbers[j] :
                index_minimum = j
        if index_minimum != i :     
            numbers[i], numbers[index_minimum] = numbers[index_minimum], numbers[i]


numbers = list(map(int, input('angka:').split(' ')))
print(f'sebelum diurutkan {numbers}')
sorting(numbers)
print(f'setelah diurutkan {numbers}')
