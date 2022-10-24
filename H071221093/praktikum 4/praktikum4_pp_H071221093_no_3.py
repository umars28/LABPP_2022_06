def CountingFactorial(angka) :
    if angka == 1 :
        return angka
    elif angka == 0 :
        return 1
    else :
        return angka * CountingFactorial(angka - 1)

angka = int(input('masukkan angka:'))
if angka == 0 :
    print(f'hasil dari faktorial {angka} =', CountingFactorial(angka))
elif angka == 1 :
    print(f'hasil dari faktorial {angka} =', CountingFactorial(angka))
else :
    print(f'hasil dari faktorial {angka} =', CountingFactorial(angka))