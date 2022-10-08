a = int(input('Nilai total belanja: '))
b = int(input('Nilai uang yang dibayar: '))
kembalian = b - a
uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
if a <= b:
    for i in uang: #range(100000, 100)
        c = kembalian // i
        print('%d uang Rp. %d '% (c, i))
        kembalian -= c * i #kembalian = (c*i) - kembalian

else:
    print('Inputan b harus lebih besar dari pada a')