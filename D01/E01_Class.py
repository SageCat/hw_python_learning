class Dog:
    __slots__ = ('name', 'age')
    dog_type = '边牧'

    def __init__(self, name=None):
        self.name = name

    def print_name(self):
        print(f"hello, my name is {self.name}")


d = Dog('哮天犬')
d.age = 10
d.address = "beijing"
d.print_name()
print(d.name)
