isinstance()
# 函数来判断一个对象是否是一个已知的类型，类似 type()。如果要判断两个类型是否相同推荐使用 isinstance()

# isinstance() 与 type() 区别：
#   type() 不会认为子类是一种父类类型，不考虑继承关系。
#   isinstance() 会认为子类是一种父类类型，考虑继承关系。

# isinstance(object, classinfo)
# object -- 实例对象。
# classinfo -- 可以是直接或间接类名、基本类型或者有它们组成的元组。

# a = 2
# isinstance (a,int)
# True

# isinstance (a,str)
# False

# isinstance (a,(str,int,list))    # 是元组中的一个返回 True
# True