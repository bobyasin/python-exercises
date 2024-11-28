class Animal:
    def walk(self):
        print("walk")


class Cat(Animal):
    def meow(self):
        print("meow")


class Dog(Animal):
    pass


dog = Dog()
cat = Cat()
dog.walk()
cat.walk()
cat.meow()