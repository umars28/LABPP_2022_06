#Tugas Program 1

class human:
    def __init__(self, name, age, isMale, tinggi):
        self.name = name
        self.age = age
        self.isMale = isMale
        self.tinggi = tinggi
    def setTinggi(self, tinggi):
        self.tinggi = tinggi
    def getTinggi(self):
        return self.tinggi
    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age
    def setname(self, name):
        self.name = name
    def getname(self):
        return self.name
    def setGender(self, isMale):
        self.isMale = isMale
    def getGender(self):
        if self.isMale == True:
            return("Male")
        elif self.isMale == False:
            return("Female")

putra = human("Putra", 18, True, 163)
putri = human("Putri",20,False,157)

print(putra.getGender())
print(putri.getGender())