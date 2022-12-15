class person :
    def __init__(self, nama, umur, perempuan) :
        self.nama = nama 
        self.umur = umur
        self.perempuan = perempuan
    def setAge (self, umur) :
        self.umur = umur
    def getAge (self) :
        print(f"Umur   : {self.umur} Tahun")
    def setName (self, nama) :
        self.nama = nama
    def getName (self) :
        print(f"Nama   : {self.nama}")
    def setGender (self, perempuan) :
        self.perempuan = perempuan
    def getGender (self) :
        if self.perempuan == 'True' or self.perempuan == 'true':
            self.perempuan = True
            if self.perempuan == True :
                print("Gender : Perempuan")
        elif self.perempuan == 'False' or self.perempuan == 'false':
            self.perempuan = False
            if self.perempuan == False :
                print("Gender : Laki-laki")
        else :
            print("inputan tidak falid")
    



name = input("Nama : ")
age = int(input("Umur : "))
isFemale = input()
human = person(name, age, isFemale)

human.getName()
human.getAge()
human.getGender()
