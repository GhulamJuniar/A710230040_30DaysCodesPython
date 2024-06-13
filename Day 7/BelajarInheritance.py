# Kelas Induk
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass harus mengimplementasikan metode ini")

    def info(self):
        return f"Saya adalah seekor {self.__class__.__name__} dan nama saya {self.name}"

# Kelas Anak yang mewarisi dari kelas Animal
class Anjing(Animal):
    def speak(self):
        return "Woof!"

# Kelas Anak yang mewarisi dari kelas Animal
class Kucing(Animal):
    def speak(self):
        return "Meow!"

# Contoh penggunaan inheritance
dog = Anjing("Lego")
cat = Kucing("Cimong")

print(dog.info())  
print(dog.speak())

print(cat.info())  
print(cat.speak()) 