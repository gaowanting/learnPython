# __dict__
#  类的静态函数、类函数、普通函数、全局变量以及一些内置的属性都是放在类__dict__里的
#  对象的__dict__中存储了一些self.xxx的一些东西

class A():
    property1 = 0
    property2 = 1

    def __init__(self, property1, property2):
        self.property1 = property1
        self.property2 = property2

    # 静态方法与类相关，但是
    # staticmethod means it doesn't need a instance to call
    @staticmethod
    def f1():
        print('this is a static function')

    # 在类A里的实例方法，第一个参数是self
    # 需要有一个类A的实例才可以调用这个方法
    def f2(self, property1, property2):
        print(f"class A has two properties, a={property1}, b={property2}")
        A.f1()

    @classmethod
    # 当我们需要和类直接交互时，而不需要和类的实例进行交互，第一个参数cls是类本身
    # 既可以用类的实例a，也可以直接用类A
    def f3(cls):
        print("this is a class function")


a = A(1, 4)
A.f1()
a.f2(A.property1, A.property2)
A.f3()

print("a.__dict__ is", end=":")
print(a.__dict__)
# a.__dict__ is:{'property1': 1, 'property2': 4}
# 列出a实例的所有属性
# 对象的__dict__中存储了一些self.xxx的一些东西

print("A.__dict__ is", end=":")
print(A.__dict__)
# A.__dict__ is:{'__module__': '__main__', 'property1': 0, 'property2': 1, '__init__': <function A.__init__ at
# 0x000002585005C550>, 'f1': <staticmethod object at 0x000002584F889400>, 'f2': <function A.f2 at
# 0x000002585005C670>, 'f3': <classmethod object at 0x000002584FF23DF0>, '__dict__': <attribute '__dict__' of 'A'
# objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
# 类的静态函数、类函数、普通函数、全局变量以及一些内置的属性都是放在类__dict__

# type(A.__dict__) <class 'mappingproxy'>
