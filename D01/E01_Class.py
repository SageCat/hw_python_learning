class Dog:
    dog_type = '边牧'

    def __init__(self, name=None):
        self.name = name

    def print_name(self):
        print(f"hello, my name is {self.name}")


d = Dog('哮天犬')
d.print_name()
print(d.name)