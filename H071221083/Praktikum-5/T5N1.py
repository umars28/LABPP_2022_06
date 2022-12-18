'''# #soal program 1
# ukuran_matriks = int(input("ukuran_matriks Matriks : "))
# matriks_1 = [[int(input(f"Matriks 1 Baris {baris + 1} dan Kolom {kolom + 1} : ")) for kolom in range(ukuran_matriks)] for baris in range(ukuran_matriks)]
# matriks_2 = [[int(input(f"Matriks 2 Baris {baris + 1} dan Kolom {kolom + 1} : ")) for kolom in range(ukuran_matriks)] for baris in range(ukuran_matriks)]
# matriks_hasil = [[0 for kolom in range(ukuran_matriks)] for baris in range(ukuran_matriks)] 
# #Matriks 3
# for x in range(ukuran_matriks):
#     for y in range(ukuran_matriks):
#         for z in range(ukuran_matriks):
#             matriks_hasil[x][y] += matriks_1[x][z] * matriks_2[z][y]
# print(f"{matriks_1} X {matriks_2} = {matriks_hasil}")

# matriks1 = [[int(input('Input nilai matriks pertama index {},{} : '. format (baris, kolom))) for kolom in range (1, 2+1)] for baris in range (1, 2+1)]
# matriks2 = [[int(input('Input nilai matriks kedua index {},{} : '. format (baris, kolom))) for kolom in range (1, 2+1)] for baris in range (1, 2+1)]
# hasil = [[0,0], [0,0]]

# def hasil_kali() :
#     hasil[0][0] = (matriks1[0][0]*matriks2[0][0]) + (matriks1[0][1]*matriks2[1][0])
#     hasil[0][1] = (matriks1[0][0]*matriks2[0][1]) + (matriks1[0][1]*matriks2[1][1])
#     hasil[1][0] = (matriks1[1][0]*matriks2[0][0]) + (matriks1[1][1]*matriks2[1][0])
#     hasil[1][1] = (matriks1[1][0]*matriks2[0][1]) + (matriks1[1][1]*matriks2[1][1])
#     print ('Hasil perkalian matriks')
#     print ('| {}, {} | X | {}, {} | = | {}, {} |'. format(matriks1[0][0], matriks1[0][1], matriks2[0][0], matriks2[0][1], hasil[0][0], hasil[0][1]))
#     print ('| {}, {} |   | {}, {} |   | {}, {} |'. format(matriks1[1][0], matriks1[1][1], matriks2[1][0], matriks2[1][1], hasil[1][0], hasil[1][1]))
#     return hasil
# hasil_kali()'''

# soal program 1
# Mengalikan 2 buah matrik 2x2

# Input
ukuran_matriks = 2
matriks_1 = [[int(input(f"Input nilai matriks pertama index {baris},{kolom} : ")) for kolom in range(ukuran_matriks)] for baris in range(ukuran_matriks)]
matriks_2 = [[int(input(f"Input nilai matriks kedua index {baris},{kolom} : ")) for kolom in range(ukuran_matriks)] for baris in range(ukuran_matriks)]
    # for baris in range(ukuran_matriks):
    #     for kolom in range(ukuran_matriks):
    #         matriks_1 = [[int(input(f"Input nilai matriks pertama index {baris},{kolom} : "))]]
        # matriks1[ ][ ]
    # for baris in range(ukuran_matriks):
    #     for kolom in range(ukuran_matriks):
    #         matriks_2 = [[int(input(f"Input nilai matriks kedua index {baris},{kolom} : "))]]
        # matriks2[ ][ ]

# wadah matriks hasil
matriks_hasil = [[0 for kolom in range(ukuran_matriks)] for baris in range(ukuran_matriks)]
    # hasil = [[0,0], [0,0]]

#operasi matriks
for x in range(ukuran_matriks):
    for y in range(ukuran_matriks):
        for z in range(ukuran_matriks):
            matriks_hasil[x][y] += matriks_1[x][z] * matriks_2[z][y]

# output
print(f"{matriks_1[0]} X {matriks_2[0]} = {matriks_hasil[0]}\n{matriks_1[1]} X {matriks_2[1]}   {matriks_hasil[1]}".replace("[", "|").replace("]", "|"))