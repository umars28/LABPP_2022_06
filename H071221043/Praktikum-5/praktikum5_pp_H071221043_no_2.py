print("Selamat datang untuk memulai silahkan input data anda")

Nama = input('Masukkan nama anda :')
Umur = input('Masukkan umur anda :')
Alamat = input('Masukkan alamat anda :')

Data = {
"Nama": Nama, 
"Umur": Umur,
"Alamat": Alamat 
}

def profil():
   print("-" * 60)
   print('Selamat datang', Data.get('Nama'), 'Silahkan pilih opsi')
   print("=" * 60)
profil()

i = 1
while i > 0 :
    print("1. Detail anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")

    print("-" * 60)
    pilihan = input('Pilih opsi yang diinginkan : ')
    print("-" * 60)

    try :
        pilihan = int(pilihan)
    except :
        ("Inputan tidak valid")
    else :
        if pilihan == 1 :
            print("Data anda adalah")
            print("Nama :", Data.get('Nama'))
            print("Umur :", Data.get('Umur'))
            print("Alamat :", Data.get('Alamat'))
            profil()
        elif pilihan == 2 :
            ubah_nama = input('Nama diubah dengan :')
            Data['Nama'] = ubah_nama
            print("Data telah diubah")
            profil()
        elif pilihan == 3 :
            ubah_umur = input('Umur diubah dengan :')
            Data['Umur'] = ubah_umur
            print("Data telah diubah")
            profil()
        elif pilihan == 4 :
            ubah_alamat = input('alamat diubah dengan :')
            Data['Alamat'] = ubah_alamat
            print("Data telah diubah")
            profil()
        elif pilihan == 5 :
            print('Selamat tinggal', Data.get('Nama'))
            break





