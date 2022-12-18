# soal program 2
# mengubah detail data

print("Selamat datang untuk memulai silahkan input data anda!")

#input data
data = list(map(str, input("Nama/Umur/Alamat : ").split('/')))

kalimat = {1 : "Data anda sukses diperbaharui."}
# list ubah data
while True:
    print('=' * 60, f"\nSelamat datang {data[0]} silahkan pilih opsi") ;  print("=" * 60)
    print("1. Detail anda\n2. Ubah Nama\n3. Ubah Umur\n4. Ubah Alamat\n5. Keluar") ;  print("=" * 60)
    opsi = int(input("Input opsi: ")) ; print("=" * 60)
    if opsi == 1: 
        print(f"Data anda adalah \nNama: {data[0]} \nUmur: {data[1]} \nAlamat: {data[2]}")
    elif opsi == 2:
        nama_baru = input("Silahkan Input nama baru : ")
        data[0] = nama_baru
        print(kalimat[1])
    elif opsi == 3:
        umur_baru = input("Silahkan Input umur baru : ")
        data[1] = umur_baru
        print(kalimat[1])
    elif opsi == 4:
        alamat_baru = input("Silahkan Input alamat baru : ")
        data[2] = alamat_baru
        print(kalimat[1])
    elif opsi == 5:
        print(f"Selamat tinggal {data[0]}")
        break