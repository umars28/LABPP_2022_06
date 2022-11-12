file_name = input('')
file_name = file_name + '.txt'
duplicate_file = input('')
duplicate_file = duplicate_file + '.txt'

temp_file = None

try :
    with open(file_name) as file :
        lines_in_file = file.readlines()

        new_file_lines = []

        for lines in lines_in_file :
            new_lines = lines.rjust(100)
            new_file_lines.append(new_lines)

        temp_file = ''.join(new_file_lines)

    with open(duplicate_file, 'w') as file :
        file.write(temp_file)
    print('berhasil')
except :
    print('gagal')
