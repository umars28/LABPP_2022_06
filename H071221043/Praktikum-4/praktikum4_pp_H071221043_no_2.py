n = int(input('Masukkan bilangan :'))

def isprime (n) :
    if (n <=1):
        return False
    for i in range (2, n):
        if (n % i == 0):
            return False
    return True

if isprime (n):
    print(n, 'adalah bilangan prima')
else:
    print(n, 'bukan bilangan prima')