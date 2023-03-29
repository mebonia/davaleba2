class People:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_gmail(self):
        print(f'{self.firstname}.{self.lastname}.school@edu.ge')


class Lecturer(People):
    def __init__(self, firstname, lastname, salary):
        super().__init__(firstname, lastname)
        self.salary = salary

    def get_gmail(self):
        print(f'{self.firstname}.{self.lastname}@edu.ge')

    def print_salry(self):
        print(f'ხელფასი:{self.salary}ლარი')


class Student(People):
    def __init__(self, firstname, lastname, courses):
        super().__init__(firstname, lastname)
        self.courses = courses

    def get_gmail(self):
        print(f'{self.firstname}.{self.lastname}.1@edu.ge')

    def course(self):
        print(', '.join(self.courses))



s1 = People('alex', "bacho")
s1.get_gmail()
s2 = Lecturer('alex', 'mebonia', '3000')
s2.get_gmail()
s2.print_salry()
s3 = Student('alex', 'menonia', ['math',  'english', 'art'])
s3.get_gmail()
s3.course()

#ნ2
class Library_item:
    def __init__(self, title, subject, status):
        self.title = title
        self.subject = subject
        self.status = status

    def booking(self):
        if self.status == 'aviable':
            print('დაჯავშნა შესრულებულია')
        elif self.status == 'ocupied':
            print('ვერ მოხერხდა დაჯავშნა რადგან ნივთი უკვე დაჯავშნულია ')


class Book(Library_item):
    def __init__(self, ISNB, authors, title, subject, status):
        super().__init__(title, subject, status)
        self.ISNB = ISNB
        self.authors = authors


class Magazine(Library_item):

    def __init__(self, jounrnalname, volume, status,title=None,subject=None):
        super().__init__(title, status,subject)
        self.journalname = jounrnalname
        self.volume = volume
        self.status = status


class CD(Library_item):
    def __init__(self, title, status, subject=None):
        super().__init__(title, status,subject)


    def booking(self):

            print('CD დაჯავშნა არ არის შესაძლებელი')


b1 = Library_item('ხევისბერი გოჩა','ქართული','aviable')
b1.booking()
b2 = Book('987-3-0','ბაჩო ფიფია','ანბანი','ქართული','aviable')
b2.booking()
m1 =Magazine('იკითხემარად','5გვერდი','ocupied')
m1.booking()
c1 = CD('ჰარიპოტერი','cdf')
c1.booking()



# N3
class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return f"გამარჯობა {self.firstname},{self.lastname} თქვენ ხართ {self.age}წლის."


class Employee:
    def __init__(self, profession, monthly_salary, working_hours):
        self.profession = profession
        self.monthly_salary = monthly_salary
        self.working_hours = working_hours

    def hourly_salary(self):
        return self.monthly_salary /(self.working_hours * 5 * 52 / 12)


class Doctor(Person, Employee):

    def __init__(self, firstname, lastname, age, profession, monthly_salary, working_hours):
        super().__init__(firstname, lastname, age)
        self.profession = profession
        self.monthly_salary = monthly_salary
        self.working_hours = working_hours

    def __str__(self):
        return f"გამარჯობა {self.firstname},{self.lastname} თქვენ ხართ {self.age}წლის."

    def hourly_salary(self):
        return self.monthly_salary / (self.working_hours * 5 * 52 / 12)


    def perfom_operation(self):
        print('ოპერაცია შესრულდა')


c1 = Doctor('alex', 'mebo', 17, 'eqimi', 6500, 8)
print(c1)
print(c1.hourly_salary(),)
c1.perfom_operation()




