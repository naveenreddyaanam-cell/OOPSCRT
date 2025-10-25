from datetime import date
class person:
    def __inti__(self,name,country,date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def calculate_age(self):
        today = date.today()
        age = today.year-self.date_of_birth.year
        if today<date(today.year,self.date_of_birth.month,self.date_of_birth.day):
            age-=1
        return age
    

person1 = person("Naveen","ongole",date(2005, 12, 7))

print("calculated age for each person")
print("********************************")
print("person 1:")
print("Name:",person1.name)
print("country:",person1.country)
print("Date of birth:",person1.date_of_birth)
print("Age:",person1.calculate_age())
