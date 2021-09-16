class Rectangle_po():
    def getPeri(self, a, b):
        return (a + b) * 2

    def getArea(self, a, b):
        return a * b

# test:
rect_po = Rectangle_po()
print(rect_po.getPeri(3, 4))
print(rect_po.getArea(3, 4))
print(rect_po.__dict__)  # 查看rect_po实例的属性

# (1)在类中不定义__init__()方法,也能定义类的实例、并且调用类的方法;
# 但是,用__dict__查看类实例的属性时,属性为空;
# 实例化类时,不需要传入初始化参数,但实例调用类的每个方法时都需要传入参数(相同参数重复传入)

# (2)在类中定义__init__()方法,创建实例时,可以为实例绑定普通字段,
# 定义和调用类方法时不再需要重复传参,更像面向对象方式的编程方式