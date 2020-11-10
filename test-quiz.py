class Dog:
    def walk(self):
        return "*walking*"


def speak(self):
    return "Woof!"


class JackRussellTerrier(Dog):
    def speak(self):
        return "Arff!"


bobo = JackRussellTerrier()
bobo.walk()
for i in range(-3, 3):
    print(i)