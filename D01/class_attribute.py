class MyClass:
    __slots__ = ['name']
    # 这是一个类属性
    class_attribute = "I am a class attribute"
    class_attribute_second = "I am second class attribute"

    def __init__(self, name):
        # 这是一个实例属性
        self.name = name


# 创建两个实例
obj1 = MyClass("Object 1")
obj2 = MyClass("Object 2")

# 修改 obj1 的类属性
obj1.class_attribute = "Modified by obj1"

# 输出 obj2 的类属性
print(obj2.class_attribute)  # 输出: "I am a class attribute"

# 修改类本身的类属性
MyClass.class_attribute = "Modified by class"
MyClass.class_attribute_second = "Second class attribute Modified by class"

# 输出 obj1 和 obj2 的类属性
print(obj1.class_attribute)  # 输出: "Modified by obj1"
print(obj2.class_attribute)  # 输出: "Modified by class"
print(obj1.class_attribute_second)  # 输出: "Second class attribute Modified by class"
print(obj2.class_attribute_second)  # 输出: "Second class attribute Modified by class"
