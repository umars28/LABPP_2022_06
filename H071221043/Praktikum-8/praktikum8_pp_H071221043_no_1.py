class person:
    def __init__(self, nama, umur, gender):
        self.nama = nama
        self.umur = umur
        self.gender = gender
    
    def getAge (self):
        print(f"umur: {self.umur} Tahun")
    
    def getName (self):
        print (f"nama: {self.nama}")
    
    def getGender (self):
        if self.gender == 'perempuan':
            self.gender = True
            if self.gender == True:
                print ("Jenis kelamin: perempuan") 
        elif self.gender == 'laki-laki':
            self.gender = False
            if self.gender == False:
                print ("Jenis kelamin: laki-laki") 
        else: 
            print("inputan salah")

name = input('masukkan nama: ')
age = int(input("masukkan umur: "))
gender = input ("masukkan gender :")

human = person(name, age, gender)

human.getName()
human.getAge()
human.getGender()