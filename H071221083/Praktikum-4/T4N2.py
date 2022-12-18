#soal program 2
def getFPB (x,y):
    if x > y :
        lebih_besar = x
    else :
        lebih_besar = y
    for i in range (1,lebih_besar + 1) :
        if x % i == 0 and y % i == 0 :
            fpb = i
    return fpb
bil1= int (input("Bilangan Pertama :"))
bil2= int (input("Bilangan Kedua :"))
print("FPB({},{})= {}".format(bil1, bil2, getFPB(bil1, bil2)))