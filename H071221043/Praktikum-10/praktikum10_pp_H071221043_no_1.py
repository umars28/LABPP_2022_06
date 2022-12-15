from praktikum10 import Menu, One, Two, Three, Four, Five, Six

satu = One()
dua = Two()
tiga = Three()
empat = Four()
lima = Five()
enam = Six()

while True:
    Menu.menu()
    opsi = input('Silahkan Pilih Opsi Anda: ')
    if opsi == '1':
        satu.pilihan()
    elif opsi == '2':
        dua.pilihan()
    elif opsi == '3':
        tiga.pilihan()
    elif opsi == '4':
        empat.pilihan()
    elif opsi == '5':
        lima.pilihan()
    elif opsi == '6':
        enam.pilihan()
        break