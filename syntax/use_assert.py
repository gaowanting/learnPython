# assert

# assert 表达式 [, 参数]
# 当表达式为真时，程序继续往下执行；
# 当表达式为假时，抛出AssertionError错误，并将  参数  输出

import test1
a = 10
assert a < 0, 'Error:a>0!'
print(a)
