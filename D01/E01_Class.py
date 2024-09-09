class Dog:
    print("我是代码块...........")
    # 显示规定实例属性被允许的名称列表
    # __slots__ = ('name', 'age')
    dog_type = '边牧'

    def __init__(self, name=None):
        print("我是 init 函数 -----------")
        self.name = name

    def print_name(self):
        print(f"hello, my name is {self.name}")


d = Dog('哮天犬')
d2 = Dog('柯基')
d.age = 10
# d.address = "beijing"
d.print_name()
print(d.name)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(Dog.__dict__)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(d.__dict__)
