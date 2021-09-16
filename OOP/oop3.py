class Stock:
    def __init__(self, ticker, price):
        self.price = price
        self.ticker = ticker
        print("this is the init function")

    def buy(self):
        print("buy a stock")

    def __del__(self):
        print("delete the object")

    def __str__(self):
        return f"this is a stock called {self.ticker}"


apple = Stock("APPLE", 10)
apple.buy()
print(apple.price)
print(apple)
# del apple
# print("-"*20)
'''
"delete the object" 在下划线下方输出
因为apple是一个全局变量
'''

