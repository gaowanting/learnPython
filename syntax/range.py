# range() 生成一个数组
# xrange() 生成一个生成器
from gevent.testing.six import xrange

print(xrange(10))
print(xrange(10, 20, 2))

print(range(10))
print(range(10, 20, 2))