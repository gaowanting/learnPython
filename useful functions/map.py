# 首先map() 是一个函数，会根据提供的函数对指定序列做映射。
# map(function, iterable, ...) --> 返回一个迭代器
#   function：定义一个函数，即映射关系
#   iterable：一个或多个序列
tuple1 = (1,2)
tuple2 = (3,4)
l1 = map(lambda x:x^2,tuple1)
l2 = map(lambda x,y:x+y ,tuple1,tuple2)
l3 = map(float, tuple1)

'''
注意这里不能print map 因为map返回的就是一个迭代器
<map object at 0x0000022A482686D0>
所以一定要变为list,tuple 或者其他
'''
print(list(l1))
print(list(l2))
print(tuple(l3))



