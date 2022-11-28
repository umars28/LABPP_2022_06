#konversi detik menjadi jam:menit:detik

#input detik dari user
while True:
    print('=========== konversi detik ke jam ===========\n')
    second = int(input('input detik\t:'))

    jam = second // 3600
    x = second % 3600
    menit = x // 60
    detik = x % 60

    print("%02d:%02d:%02d" % (jam, menit, detik))

