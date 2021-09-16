def demo():
    """ this is a demo function"""
    print(123)


print(demo.__doc__)

'''
print(dir(demo))
    # __方法名__ 格式是python内置的属性/方法 
    # 利用dir函数快速查看方法列表
['__annotations__', '__call__', '__class__',
 '__closure__', '__code__', '__defaults__',
'__delattr__', '__dict__', '__dir__', 
'__doc__', '__eq__', '__format__', 
'__ge__', '__get__', '__getattribute__',
'__globals__', '__gt__', '__hash__',
'__init__', '__init_subclass__', '__kwdefaults__', 
'__le__', '__lt__', '__module__', 
'__name__', '__ne__', '__new__', 
'__qualname__', '__reduce__', '__reduce_ex__', 
'__repr__', '__setattr__', '__sizeof__', 
'__str__', '__subclasshook__']
'''
