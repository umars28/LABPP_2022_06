print('Selamat datang untuk memulai silahkan input data anda')
nama = input('Input nama : ')
umur = int(input('Input umur : '))
alamat = input('Input alamat : ')
daftar_data = {
    'nama' : nama,
    'umur' : umur,
    'alamat' : alamat 
}
while True : 
    print('='*50)
    print('Selamat datang {} silahkan pilih opsi'. format (daftar_data['nama']))
    print('='*50)
    print('''
1. Detail anda
2. Ubah nama
3. Ubah umur
4. Ubah alamat
5. Keluar
    ''')
    print('='*50)
    opsi = int(input('Input opsi : '))
    if opsi == 1 :
        print('='*50)
        print(f'Data anda adalah \nNama : {daftar_data["nama"]} \nUmur : {daftar_data["umur"]} \nAlamat : {daftar_data["alamat"]}')
    elif opsi == 2 :
        ubah_nama = input('Silahkan input nama baru : ')
        daftar_data['nama'] = ubah_nama
        print('Data berhasil diperbarui')
    elif opsi == 3 :
        ubah_umur = input('Silahkan input umur baru : ')
        daftar_data['umur'] = ubah_umur
        print('Data berhasil diperbarui')
    elif opsi == 4 : 
        ubah_alamat = input('Silahkan input alamat baru : ')
        daftar_data['alamat'] = ubah_alamat
        print('Data berhasil diperbarui')
    elif opsi == 5 :
        print('='*50)
        print('Selamat tinggal {}'. format(daftar_data['nama']))
        break
    else : 
        print('Invalid') 