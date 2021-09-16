import numpy as np
import pandas as pd

# ====Series=====
s1 = pd.Series([1, 2, 3], index=('a','b','c') )
print(s1)

s2 = pd.Series(np.random.randn(5))
print(s2)

# create Series use a dict
s3 = pd.Series({'Math': 99, "English": 90, "Physics": 95})
print(s3)

d = {"a": 0.0, "b": 1.0, "c": 2.0}
pd.Series(d)
# if an index is passed, the values in data corresponding to the labels in the index will be pulled out.
s = pd.Series(d, index=["b", "c", "d", "a"])

# if data is a scalar value, an index must be provided, the value will be repeated to match the length of index.
print(pd.Series(5.0, index=list("hello")))

print('===series is ndarray-like===')
# slicing -- it will also slice the index
print(s2[3:])  # [] slice by the number of index
print(s2[s2 > s2.mean()])
print(s2[[1, 4]])  # [[]] slice by the name of index
print(np.exp(s2))  # e的x幂次方

# if I need a array(do some operation without the index), just use s.array
print(s2.array)
print(type(s2.array))  # <class 'pandas.core.arrays.numpy_.PandasArray'>


print('===array and ndarray===')
# array是一个函数，用来创建一个矩阵对象
a = np.array([[1,2,3,4],[0,0,0,0],[1,2,4,3]])
print(a)
print(type(a)) # <class 'numpy.ndarray'> ndarray是一个类型
# if I need an actual ndarray, then use Series.to_numpy()
a2 = s2.to_numpy() # this will create a ndarray
print(a2)
print(type(a2))

print('===Series is dict-like===')
print(s1['a'])
print('b' in s1)  # True
print('d' in s1)  # False
# s1['d']  # the label is not contained, an exception is raised
s1.get('d')  # a missing label will return None or specified default

print('===Vectorized operations===')
s2+s2
s1*2
np.exp(s2)
print('===label alignment===')
# a key difference betweem Series and a ndarray is that
# operations between Series automatically align the data based on label
print(s2[1:] + s2[:-1])

print('===Name attribute===')
s4 = pd.Series(np.random.rand(5), name='something')
print(s4.name)
s5 = s4.rename('diff')
print(s4.name)  # something : rename can't change the original objects
print(s5.name)  # diff : but it can name a new object

print("===useful functions===")
# 可以理解为给Series去重
s4.unique()
