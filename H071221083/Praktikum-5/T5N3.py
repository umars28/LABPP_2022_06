#soal program 3
#Mencari Nilai Duplikat 2 Array

# input
x = set(map(int, input("List 1 : ").split()))
y = set(map(int, input("List 2 : ").split())) ; n = []

# olah
for i in x:
    if i in y:
        if i not in n:
            n.append(str(i))
if len(n) == 0:
    print("Tidak ada duplikat!")

# output
print(f"Terdapat {len(n)} buah duplikat yaitu ({','.join(n)})")