personal_data =[] 

print('=================================')
print('     isi data diri anda')
print('=================================')
name = personal_data.append(input('masukkan nama:'))
age = personal_data.append(input('masukkan umur:'))
address = personal_data.append(input('masukkan alamat:'))
print('=================================\n')
print(personal_data)
def menu() :
    print('=================================')
    print('     silahkan pilih opsi')
    print('=================================')
    print('1. data diri anda\n2. ubah nama\n3. ubah umur\n4. ubah alamat\n5. keluar')
    print('=================================\n')

menu()
choosedoption = int(input('pilih opsi:'))
print('=================================\n')

while True :
    if choosedoption == 1 :
        print('=================================')
        print('         data diri anda')
        print('---------------------------------')
        print('nama:', personal_data[0])
        print('umur:', personal_data[1])
        print('alamat:', personal_data[2])
        print('=================================\n')
        menu()
        choosedoption = int(input('pilih opsi:'))
        print('=================================\n')
    if choosedoption == 2 :
        print('=================================')
        print('           ubah nama')
        print('---------------------------------')
        personal_data[0] = input('masukkan nama:')
        print('---------------------------------')
        print('  berhasil mengubah nama anda') 
        print('=================================\n')
        menu()
        choosedoption = int(input('pilih opsi:'))
        print('=================================\n')
    if choosedoption == 3 :
        print('=================================')
        print('           ubah umur')
        print('---------------------------------')
        personal_data[1] = input('masukkan umur:')
        print('---------------------------------')
        print('  berhasil mengubah umur anda') 
        print('=================================\n')
        menu()
        choosedoption = int(input('pilih opsi:'))
        print('=================================\n')
    if choosedoption == 4 :
        print('=================================')
        print('          ubah alamat')
        print('---------------------------------')
        personal_data[2] = input('masukkan alamat:')
        print('---------------------------------')
        print('  berhasil mengubah alamat anda') 
        print('=================================\n')
        menu()
        choosedoption = int(input('pilih opsi:'))
        print('=================================\n')
    if choosedoption == 5 :
        print('=============================================')
        print('  terimakasih telah menggunkan program ini')
        print('=============================================')
        break
    if choosedoption > 5 or choosedoption <=0 :
        print('=================================')
        print('      opsi tidak tersedia')
        print('=================================\n')
        menu()
        choosedoption = int(input('pilih opsi:'))
        print('=================================\n')