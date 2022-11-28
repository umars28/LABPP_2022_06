#program konversi angka ke huruf

input_nilai = int(input('masukkan nilai:'))
konversi = 'A' if input_nilai >= 90 else 'B' if input_nilai >= 80 else 'C' if input_nilai >= 70 else 'D' if input_nilai >= 60 else 'E' if input_nilai >= 40 else 'F'

print('nilai', input_nilai, '=', konversi)
