#soal program 1
#input nilai
nilai = input("Nilai : ")

#using exception if it's not int
try:
    nilai = int(nilai)
except :
    print("Nilai harus angka") 
    quit()

#convert with elif
if nilai >= 90:
    peringkat = 'A'
elif nilai >= 80:
    peringkat = 'B'
elif nilai >= 70:
    peringkat = 'C'
elif nilai >= 60:
    peringkat = 'D'
elif nilai >= 40:
    peringkat = 'E'
elif nilai < 40:
    peringkat = 'F'

#print output
print("Nilai {} = '{}'.". format(nilai,peringkat))