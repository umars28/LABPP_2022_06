a = input()
b = input()

try:
    with open(f"{a}.txt","r") as f:
        c = f.read()
        w = open(f"{b}.txt","w")
        w.write(c)
        print("Berhasil")
except:
        print("Gagal")









