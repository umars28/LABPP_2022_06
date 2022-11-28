class Person:
    def __init__(self, name, age, isMale):
        self.name = name
        self.age = age
        self.isMale = isMale

    def setAge (self, age):
        self.age = int(age)
    def getAge (self):
        return self.age

    def setName (self, name):
        self.name = name 
    def getName (self):
        return self.name
        
    def setGender (self):
        if self.isMale == "TRUE":
            self.isMale = True
        else:
            self.isMale = False 
    def getGender (self):
        if self.isMale == True:
            self.isMale = "male"
        else:
            self.isMale = "female"
        return self.isMale

name = input ("insert name: " )
Age = int(input ("insert age: "))
isMale = input ("are you male? True or False: ").upper()
if isMale == "TRUE":
    isMale = bool(True)
else:
    isMale = bool(False)

person = Person(name, Age, isMale)
print(person.getName())
print(person.getAge())
print(person.getGender())

