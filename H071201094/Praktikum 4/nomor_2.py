def bil() :
    n = int(input("Bilangan bulat : "))
    prima = True
    for i in range (2, n) :
        if n % i == 0 :
            prima = False
            print("Bukan bilangan prima ")
            break
    if prima == True :
        print("Bilangan prima ")