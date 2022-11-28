def number2():
    n = int(input("bilangan bulat: "))
    prima = True
    for i in range (2, n):
        if n % i == 0:
            prima = False
            print ("ini bukan bilangan prima ")
            break
    if prima == True:
        print ("ini bilangan prima")
     