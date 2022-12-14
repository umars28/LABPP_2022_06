list1 = [int(input("Input nilai matriks pertama indeks 1,1 : ")),
int(input("Input nilai matriks pertama indeks 1,2 : ")),
int(input("Input nilai matriks pertama indeks 2,1 : ")),
int(input("Input nilai matriks pertama indeks 2,2 : "))]

list2 = [int(input("Input nilai matriks kedua indeks 1,1 : ")),
int(input("Input nilai matriks kedua indeks 1,2 : ")),
int(input("Input nilai matriks kedua indeks 2,1 : ")),
int(input("Input niali matriks kedua indeks 2,2 : "))]

a = list1[0]*list2[0] + list1[1]*list2[2]
b = list1[0]*list2[1] + list1[1]*list2[3]
c = list1[2]*list2[0] + list1[3]*list2[2]
d = list1[2]*list2[1] + list1[3]*list2[3]

print("Hasil perkalian matriks : ")
print("|%d, %d| x |%d, %d| = |%d, %d|" %(list1[0],list1[1],list2[0],list2[1],a,b))
print("|%d, %d|   |%d, %d|   |%d, %d|" %(list1[2],list1[3],list2[2],list2[3],c,d))