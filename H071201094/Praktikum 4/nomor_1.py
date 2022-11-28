def sorting(numbers) :
    for i in range(len(numbers)) :
        index_minimum = i
        for j in range(i+1, len(numbers)) :
            if numbers[index_minimum] > numbers[j] :
                index_minimum = j
        if index_minimum != i :
            numbers[i], numbers[index_minimum] = numbers[index_minimum], numbers[i]
            
while True :
    numbers = list(map(int, input("Angka : "). split(" ")))
    print(f"Sebelum diurutkan {numbers} ")
    sorting(numbers)
    print(f"Setelah diurutkan {numbers} ")
    print(" ")