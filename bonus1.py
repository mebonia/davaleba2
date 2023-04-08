# N2
safexuri = int(input("საფეხურების რაოდენობა: "))


def kibe(m):
    if m <= 1:
        return m
    else:
        return kibe(m - 1) + kibe(m - 2)


def ways(step):
    return kibe(step + 1)


print(f" კიბეზე ასვლის {ways(safexuri)} გზა არსებობს")


# an es variantic.

def climbStairs(n=int(input(':'))):
    if n == 1 or n == 2 or n == 3:
        return n
    prevprev = 1
    prev = 2
    current = 0

    for step in range(3, n + 1):
        current = prevprev + prev
        prevprev = prev
        prev = current
    return current


print(climbStairs())

# N1
from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        m = (other.x - self.x) ** 2 + (other.y - self.y) ** 2

        return sqrt(m)


a = int(input(':'))
b = int(input(':'))
num1 = Point(a, b)
k = (int(input(':')))
j = (int(input(':')))
num2 = Point(k, j)
jami = num1 + num2
print(num1.__add__(num2))


# N3
def roman_to_integer(s: str) -> int:
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    n = 0

    for c in s[::-1]:
        current = roman_dict[c]

        if current < n:
            result -= current
        else:
            result += current

        n = current

    return result


print(roman_to_integer('III'))
print(roman_to_integer('IV'))
print(roman_to_integer('IX'))
print(roman_to_integer('LVIII'))
print(roman_to_integer('MCMXCIV'))


# N4
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def __mul__(self, scalar):
        if not isinstance(scalar, int):
            raise TypeError("სკალარი აუცილებლად უნდა იყოს ინტეჯერის ტიპის")
        return scalar * self.x, scalar * self.y
        # return Vector(scalar * self.x, scalar * self.y)


num1 = Vector(1, 5)
num2 = Vector(2, 3)
print(num1.__add__(num2))
print(num1.__mul__(3))
