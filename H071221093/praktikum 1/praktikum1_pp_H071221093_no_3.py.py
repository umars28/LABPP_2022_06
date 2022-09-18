#konversi wH ke kwH
print('nama\t: shaff shalihin\nNIM\t: H071221093\n')

#input pemakaian listrik dalam wH
while True:
    print('============== tagihan listrik bulanan ==============\n')
    listrik1 = int(input('input pemakaian listrik (wH)\t:'))
    print('------------------------')
    listrik2 = listrik1 / 1000 * 30

    TotalTagihan = listrik2 * 1325

    print('tagihan bulanan anda\t\t:Rp.', round(TotalTagihan, 2))

