class Cat:
    # constructor
    # python does not support constructor overloading
    def __init__(self, name):
        self.name = name

    def run(self):
        print("Cat is running")

    def jump(self):
        print("Cat is jumping")


new_cat = Cat("Sarman")
new_cat.run()
new_cat.jump()
# new_cat.name = "Cincin"  # attr can be set dynamically

print(new_cat.name)

second_cat = Cat("Tekir")
print(second_cat.name)