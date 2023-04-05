#N3
class Plane:
    def Move(self):
        print("Plane can fly")

    def Speed(self):
        print("Its speed is up to 900km/h")


class Bus:
    def Move(self):
        print("Bus can move on roads")

    def Speed(self):
        print("Its speed is up to 180km/h")


def movement(obj):
    obj.Move()
    obj.Speed()



plane = Plane()
bus = Bus()
movement(plane)
movement(bus)


# N1

class Currency:
    exchange = {"GEL": 1.0, "EUR": 2.779, "USD": 2.53}

    def __init__(self, value, unit="GEL"):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value:.2f} {self.unit}"

    def change_to(self, new_unit):
        if self.unit == "GEL" and new_unit == "USD":
            new_value = self.value / 2.53
            return Currency(new_value, new_unit)
        elif self.unit == "GEL" and new_unit == "EUR":
            new_value = self.value / 2.779
            return Currency(new_value, new_unit)
        elif self.unit == "USD" and new_unit == "GEL":
            new_value = (self.value * 2.53)
            return Currency(new_value, new_unit)
        elif self.unit == "USD" and new_unit == "EUR":
            new_value = (self.value * 2.53) / 2.779
            return Currency(new_value, new_unit)
        elif self.unit == "EUR" and new_unit == "GEL":
            new_value = (self.value * 2.779)
            return Currency(new_value, new_unit)
        elif self.unit == "EUR" and new_unit == "USD":
            new_value = (self.value * 2.779) / 2.53
            return Currency(new_value, new_unit)
        elif self.unit == new_unit:
            return self
        else:
            raise ValueError(f"Cannot convert from {self.unit} to {new_unit}")

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.unit == other.unit:
                return Currency(self.value + other.value, self.unit)
            else:
                converted_value = other.change_to(self.unit).value
                return Currency(self.value + converted_value, self.unit)

    def __mul__(self, other):
        if other is int or float:
            new_value = self.value * other
            return Currency(new_value, self.unit)
        else:
            raise TypeError('გამრავლების ოპერაცია სრულდება მხოლოდ მთელ ან ათწილად რიცხვზე')

    def __gt__(self, other):

        if isinstance(other, Currency):
            if self.unit == other.unit:
                return self.value > other.value
            elif self.unit == "GEL" and other.unit == "USD":
                return self.value > other.value * self.exchange[other.unit]
            elif self.unit == "GEL" and other.unit == "EUR":
                return self.value > other.value * self.exchange[other.unit]
            elif self.unit == "USD" and other.unit == "EUR":
                return self.value > (other.value / self.exchange[self.unit]) * self.exchange[other.unit]
            elif self.unit == "EUR" and other.unit == "USD":
                return self.value > (other.value / self.exchange[self.unit]) * self.exchange[other.unit]


ob1 = Currency(118, "USD")
ob2 = Currency(100, "EUR")
print(ob1)
print(ob2)
print('chnageTo მეთოდი', ob2.change_to("GEL"))
print('add მეთოდი', ob1.__add__(ob2))
print('გამრავლების ოპერაცია', ob2.__mul__(6))
print('შედარების მეთოდი:', ob1.__gt__(ob2))


# N2

class Person:

    def __init__(self, name, deposit=100, loan=0, owner=None):
        self.name = name
        self.deposit = deposit
        self.loan = loan
        self.owner = owner

    def __str__(self):
        return f"Name:{self.name} Deposit:{self.deposit} Loan:{self.loan}"


class House:
    def __init__(self, ID, price, ownerName, status='for sale'):
        self.ID = ID
        self.price = price
        self.owner = ownerName
        self.status = status

    def sell_house(self, buyeR, loan=None):
        if loan is not None:
            self.owner.deposit += self.price
            self.owner, buyeR = buyeR, self.owner
            self.status = 'sold on loan'
            buyeR.loan += loan
            return f"house with ID {self.ID}and price{self.price} is sold to {buyeR.name} on a loan of {loan}"
        else:
            self.owner.deposit += self.price
            buyeR.deposit -= self.price
            self.owner, buyeR = buyeR, self.owner
            self.status = "sold"
            return f"house with ID {self.ID} is sold to {self.owner.name}"


mflobeli = Person('gocha')
buyer = Person('bacho', 500)

bina = House('123-456', 250, mflobeli)
print(mflobeli)
print(buyer)
print(bina.sell_house(buyer))
print(mflobeli)
print(buyer)

print(bina.sell_house(buyer, 1000))
print(mflobeli)
print(buyer)
