# 定义只包含方法的类
"""
class 类名:
    def func1(self, parameters):
        pass

    def func2(self, parameters):
        pass
"""
# 创建对象
"""
对象变量 = 类名()
"""


class Cat:

    def drink(self):
        print("I wanna to drink water!")

    def eat(self):
        print("fish~ fish~")

# create Cat Object
cat1 = Cat()
cat1.eat()
cat1.drink()

print(cat1)
# <__main__.Cat object at 0x000001B93996B100>

addr = id(cat1)
print("%x" % addr)
# %x 表示十六进制输出
# %d 表示十进制输出

cat2 = Cat()
cat2.eat()
cat2.drink()
print(cat2)
# <__main__.Cat object at 0x00000212F01DB520>
cat3 = cat2  # 在内存中属于同一个对象，但是贴着不同的标签
print(cat3)
# <__main__.Cat object at 0x000001ABD1C8B520>


# 在类的外部用.的方式为对象附一个属性
cat1.name = "Kitty"
cat2.name = "tom"  # 此时cat2，cat3属于同一个对象，因此属性会同时赋值
print(cat1.name)