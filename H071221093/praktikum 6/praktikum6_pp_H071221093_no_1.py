file_name = input('')
file_name = file_name + '.txt'
duplicate_file = input('')
duplicate_file = duplicate_file + '.txt'

temp_file = None

try:
    with open(file_name) as file :
        temp_file = file.read()

    with open(duplicate_file, 'w') as file :
        file.write(temp_file)
    
    print('berhasil')
except:
    print('gagal')
