class Jharkhand:
    def capital(self):
        print("Ranchi")
    def language(self):
        print("Hindi and English")

class Bihar:
    def capital(self):
        print("Patna")
    def language(self):
        print("Hindi and English and Bhojpuri")

# Creating objects:
obj1 = Jharkhand()
obj2 = Bihar()

# Use for loop to access different objects.
for state in (obj1, obj2):
    state.capital()
    state.language()
