#soal program 3
#input int variable
A = int(input("Masukkan nilai variabel A: "))
B = int(input("Masukkan nilai variabel b: "))
C = int(input("Masukkan nilai variabel c: "))

#using elif else to compare variable values
if A > B and A > C:
  nilai_terbesar = A
elif B > A and B > C:
  nilai_terbesar = B
else:
  nilai_terbesar = C

#print output
print("{} adalah nilai terbesar.". format(nilai_terbesar))