class Celsius:
    def __init__(self,temperature):
        self.__temperature = temperature

    def get_temp(self):
        return self.__temperature
    def set_temp(self, new_temp):
        self.__temperature = new_temp
    def del_temp(self):
        del self.__temperature

    temperature = property(get_temp,set_temp, del_temp)
cels1,cels2 = Celsius(2),Celsius(4)
print('პირველი ობიექტი',cels1.temperature,'\n მეორე ობიექქტი',cels2.temperature)
cels1.set_temp(8)
cels2.set_temp(18)
print('პირველი ობიექტი',cels1.temperature,'\n მეორე ობიექტი',cels2.temperature)
del(Celsius.temperature,Celsius.temperature)
print(cels1.temperature,cels2.temperature)





#N2
class Bank_Account:
    def __init__(self,account_name, balance=0):
        self.__account_name=account_name
        self.__balance=balance

    def __str__(self):
        return f"გამარჯობა {self.__account_name}, თქვენ ანგარიშზე გაქვთ:{self.__balance} ლარი."
    def get_name(self):
        return self.__account_name
    def set_name(self, new_accountname):
        self.__account_name = new_accountname
    def deposit(self, amount):
        self.__balance += amount
        print(f'ბალანსზე თანხის შეტანა წარმატებით განხორციელდა, ამჟამად ანგარიშზე გაქვთ: {self.__balance} ლარი')
    def withdraw(self, withdraw):
        self.__balance -= withdraw
        print(f'თანხის გამოტანა შერსულებულია. ამჟამად ანგარიშჟე გაქვთ {self.__balance} ლარი')


my_account = Bank_Account('alex',70)
print(my_account)
my_account.deposit(int(input('განახორციელეთ სასურველი თანხის შეტანა ანგარიშზე:')))
my_account.withdraw(int(input('განახორციელეთ სასურველი თანხის გამოტანა:')))

#N3
from math import sqrt
class Point:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def distance(self):

        return sqrt((self.x)**2+(self.y)**2)

point1=Point(3,5)
point2=Point(6,9)
print(point1.distance())
print(point2.distance())

#ბონუსი

class Fraction:
    def __init__(self,top,bottom):
        self.top =top
        self.bottom = bottom
    def __str__(self):
        return f"{self.top}/{self.bottom}"
    def jami(self,erti, ori):
        top = erti.top * ori.bottom + ori.top * erti.bottom
        botom = erti.bottom * ori.bottom
        return Fraction(top,botom)

    # ესეც  ერთ-ერთი ვარიანტი მაგრამ ვერ ავამუშავე  #return Fraction(((erti.top * ori.bottom) + (ori.top * erti.bottom)) / (erti.bottom * ori.bottom))
    def inferse(self):
        return f'{self.bottom}/{self.top}'
num1 = Fraction(2,5)
num2 = Fraction(4,7)
print('ჯამი',num1.jami(num1,num2))
print('შებრუნებული მნიშვლენობა',num1.inferse(),num2.inferse())



























