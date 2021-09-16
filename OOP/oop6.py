class Coffee:
    def __init__(self, name, temper):
        self.name = name
        self.temper = temper
        # 私有属性，在外界不可以被直接访问
        # 在对象的方法内部，是可以访问对象的
        self.__volume = 500

    def buy(self):
        print(f"this is a {self.name}")

    # 私有方法同样不允许在外界直接访问
    def __add(self):
        self.__volume += 100

    def get_volume(self):
        self.__add()
        return self.__volume


cup1 = Coffee("Latte", "cold")
cup1.buy()
cup1._Coffee__add() # 这样强行访问也不是不行
print(cup1.get_volume())

