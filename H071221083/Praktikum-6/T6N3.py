#soal program 3
#data asisten lab pp

x = input()+'.txt'
y = int(input())

try:
    with open("Tabel.txt", "w"), open("Tabel.txt", "r") as tabel:
        file_as = tabel.read()
        with open(x, "w") as konten:
            konten.write(file_as)
            konten.write("+--------------------------------+---------------+------------+\n+              Nama              +      NIM      + Angkatanan +\n+--------------------------------+---------------+------------+\n")
            for i in range(y):
                a,b,c = input().replace(" ", "_"), input(), input()
                if len(a) <= 20 and len(b) <= 11 and len(c) <= 4:
                    konten.write(f"|{a.ljust(32)}|{b.ljust(15)}|{c.ljust(12)}|\n+--------------------------------+---------------+------------+\n")
                else:
                    raise Exception()
except: 
    print("Gagal!")