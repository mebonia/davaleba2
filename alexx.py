class Rectangle:
    def __init__(self,width,lenght,color):
        self.width=width
        self.lenght=lenght
        self.color=color
    def perimeter(self):
        return 2 *(self.width + self.lenght)
    def area(self):
        return self.lenght * self.width
obj_1 = Rectangle(5,1,'blue')

obj_2 = Rectangle(3,3,"green")
obj_3 = Rectangle(7,3,"purple")
print('obj_1-ის ფართობი:',obj_1.area())

#N2
class Car:
    def __init__(self,brand, color, model):
        self.color = color
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"car brand {self.brand}, car model {self.model}, car color {self.color}"
car1 = Car("red","ford","mustang")
car2 = Car("blue", "Toyota","prius")
car3 = Car("green", "voskswagen", "Golf")
print(car1)
print(car2)
print(car3)

#N3
class Dog:
    def __init__(self, breed= 'ლაგვადორი' , size = 'საშუალო' , age =3, color = 'შავი'):
            self.color=color
            self.breed=breed
            self.size=size
            self.age=age

    def eat(self):
        return "ჭამს შემწვარ ქათამს :)"
    def sleep(self):
        return "სძინავს 5საათი"
    def sit(self):
        return "ზის ლოგინზე"
    def run(self):
        return "დარბის 20კმ/სთ-ით"
    def __str__(self):
        return f"ძაღლის ჯიში:{self.breed} \nძაღლის ზომა: {self.size} \nძაღლის ასაკი:{self.age} \nძაღლის ფერი:{self.color} \n"
dog1=Dog('Neapolitan Mastiff','large','5 years', 'black')
dog2 = Dog('Maltese','small','2 years','white')
dog3 = Dog('Chow Chow','Midium','3 years','brown')
print(dog1,dog1.sleep(),dog1.eat(),dog1.sit(),dog1.run())
print('მე-2 ძაღლი\n', dog2,dog2.eat(),dog2.sit(),dog2.run(),dog2.sleep())
print('მე-3ძაღლი \n', dog3, dog3.eat(),dog3.sleep(),dog3.run(),dog3.sit())
print(Dog())## გაჩუმებითი პარამეტრიც მუშაობს :)






