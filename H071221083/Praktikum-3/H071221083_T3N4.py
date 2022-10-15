#soal program 4
#input rows
rows = input("masukkan jumlah baris : ")

rows = int(rows) + 1 # +1 cuz it start from 0

#using nested loop to print star & set new row
for star in range(rows): 
    #make a blank
    for b in range(rows-1): #karena dimulai dari 0 sampai 5, terhitung ada 6. jadi rows-1
        print(" ",end=" ") #buat spasi
    rows -= 1  #spasinya berkurang 1 tiap baris baru
    #buat bintangnya terhitung ganjil
    for j in range(star*2-1) : # rule = 2n-1 -> cari ganjil
        print("*",end=" ") #print star
    print() #print new row


# #input number of rows
# rows = (int(input("Masukkan jumlah baris = ")))
# # rows = 5
# for a in range (1, rows + 1):
# # for a in range (1, rows + 1): -> for a in range(1,6):
#     print ((rows-a) * " " + (a * "* "))
#     # print ((5-1) * " " + (1 * "* "))
#     # print ((5-2) * " " + (2 * "* "))
#     # print ((5-3) * " " + (3 * "* "))
#     # print ((5-4) * " " + (4 * "* "))
#     # print ((5-5) * " " + (5 * "* "))    