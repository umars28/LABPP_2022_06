def IsPrima(a) :
    for i in range(2, a) :
        if a % i == 0 :
            return False
    return True

bilangan = int(input('angka:'))
prima = prima(bilangan)

if bilangan == 0 or bilangan == 1 :
    print('bukan bilangan prima')
elif prima == True :
    print('bilangan prima')
else:
    print('bukan bilangan prima')
