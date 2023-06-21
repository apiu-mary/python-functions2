from typing import Any


class AnkaraDesign:
    def __init__(self,mood,temperature):
        self.mood=mood
        self.temperature=temperature
    def predict_Design(self,design):
            self.design=design
            if self.temperature in range(10,30) and self.mood=="happy":
               return f"pattern changes to {design}"
            elif self.temperature in range(30,40) and mood=="happy":
                return f"pattern changes to {design}"
            else:
                return f"pattern remains the same"
        

class Drum:
    def __init__(self,material,size):
        self.materail=material
        self.size=size

    def produce_sound(self,tone):
        return f"produces {tone} and has {self.materail} and {self.size} size"
class Djembe(Drum):
   def produce_sound(tone):
       return  f"produces {tone}"
class TalkingDrum(Drum) :
    def playsound(self,tone):
        return f"produces {tone} "  
class  Bogarabou(Drum):
    def playsound(self,tone):
        return f"produces {tone}"    
   

obt=Drum("leather","medium")
print(obt.produce_sound("tutut"))



# class Book:
#     def __init__(self,title,author,publicationyear):
#         self.title=title
#         self.author=author
#         self.publicationyear=publicationyear
#     def read_book(self):
#         return "I have read {self.title} by{self.author} in the year {self.year}"
# class Novel(Book):
#     super(title,author,publicationyear,genre):
#     self.genre=genre
#     def readnovel(self):
#         return f"i have read {self.title} by {self.author} published in {self.genre}"


class Book:
    def __init__(self, title, author, publicationyear):
        self.title = title
        self.author = author
        self.publicationyear = publicationyear
    
    def read_book(self):
        return f"I have read {self.title} by {self.author} in the year {self.publicationyear}"

class Novel(Book):
    def __init__(self, title, author, publicationyear, genre):
        super().__init__(title, author, publicationyear)
        self.genre = genre
    
    def read_novel(self):
        return f"I have read {self.title} by {self.author} published in {self.genre}"
class Magazine(Book):
    def __init__(self, title, author, publicationyear,issuenumber):
        super().__init__(title, author, publicationyear)  
        self.issuenumber=issuenumber
    def readMagazine(self): 
        return f"I have read {self.issuenumber}by {self.author}, by {self.publicationyear},by {self.author}"
class Textbook(Book):
    def __init__(self, title, author, publicationyear,number):
        super().__init__(title, author, publicationyear)  
        self.number=number  
    def read_book(self):
        return super().read_book()    
   
        
obj1=Book("Born a Crime","Trevor",1992)
print(obj1.read_book())
obj2=Magazine("Think and grow rich","Noepoleon",9934,20)
print(obj2.readMagazine())
obj3=Textbook("Cri","Mary",1999,24)
print(obj3.read_book())    
class  Animal:
    def __init__(self,name,age,habitat):
        self.name=name
        self.age=age
        self.habitat=habitat
    def  printdetails(self):
        return f"{self.name} of {self.age} and {self.habitat}" 
class Mammals(Animal):
    def __init__(self, name, age, habitat,gestation):
        super().__init__(name, age, habitat) 
        self.gestation=gestation     
        