print("\nSelamat datang untuk memulai silahkan input data anda")

nama = input("Input Nama : ")
umur = int(input("Input Umur : "))
alamat = input("Input Alamat : ")

data = {
"Nama": nama, 
"Umur": umur,
"Alamat": alamat 
}

def profil():
    print("========================================================")
    print('Selamat datang', data.get('Nama') ,'silahkan pilih opsi')
    print("========================================================")
profil()

i = 1
while i > 0 :
    print("1. Detail anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")

    print("========================================================")
    a= input("Input opsi : ")
    print("========================================================")

    try :
        a = int(a)
    except :
        print("Inputan salah")
    else:
        if a == 1:
            print("Data anda adalah")
            print('Nama :', data.get('Nama'))
            print('Umur :', data.get('Umur'))
            print('Alamat :', data.get('Alamat'))
            profil()
        elif a == 2:
            nama_baru = input("Silahkan input nama baru : ")
            data['Nama'] = nama_baru
            print("Data anda sukses di perbarui")
            profil()
        elif a == 3:
            umur_baru = input("Silahkan input umur baru : ")
            data['Umur'] = umur_baru
            print("Data anda sukses di perbarui")
            profil()
        elif a == 4:
            alamat_baru = input("Silahkan input alamat baru : ")
            data['Alamat'] = alamat_baru
            print("Data anda sukses di perbarui")
            profil()
        elif a == 5:
            print('Selamat Tinggal', data.get('Nama'))
            break