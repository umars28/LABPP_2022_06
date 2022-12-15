print("Masukkan nilai x dan y (x < y)")
x = int(input("Nilai x : "))
y = int(input("Nilai y : "))
if x < y :
    for i in range(1, y + 1 ) :
        print(i, end = " ")
        if i % x == 0 :
            print()
else :
    print("y Harus lebih besar dari x ")