class Person:


    def __init__(self, age, gender, normal_heart_rate):
        self.age = age
        self.gender = gender
        self.normal_heart_rate = normal_heart_rate

    def __str__(self):
        return f"age {self.age}, gender: {self.gender}, heart rate: {self.normal_heart_rate} bpm"

    def avg_life_expectancy(self):
        sahs_xangrdzlivoba =2600000000/self.normal_heart_rate/60/24/365
        return sahs_xangrdzlivoba

    def max_heart_rate(self):
        if self.gender == 'F':
            max_heart_rate = 226 - 0.9 * self.age
        elif self.gender == 'M':
            max_heart_rate = 223 - 0.9 * self.age
        return max_heart_rate

    def max_guliscemavarjishisas(self, intensity_level):
        if intensity_level == "ინტენსიური":
            factor = 0.8
        elif intensity_level == "საშუალო დატვირთვისას":
            factor = 0.6
        elif intensity_level == "დამწყებისთვის":
            factor = 0.5
        max_hart_varjishisas = (self.max_heart_rate() - self.normal_heart_rate) * factor + self.normal_heart_rate
        return max_hart_varjishisas

person = Person(30, 'M', 70)
print(person)
print('სიცოცხლის საშ. ხანგრძლივობა',person.avg_life_expectancy())
print('მაქსიმალური გულისცემა',person.max_heart_rate())
print('მაქს. გულისცემა ფიზიკური ვარჯიშისას',person.max_guliscemavarjishisas('საშუალო დატვირთვისას'))
