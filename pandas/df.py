import pandas as pd
import numpy as np

print('====what is a dataframe====')
# df is a 2-dim labeled data structure with columns of potentially different types

print('====create a dataframe====')
# use a dictionary(1D ndarrays, lists, dicts, or Series)
d = {"Math": [100, 99, 89],
     "Chemistry": [98, 80, 78],
     "Physics": [90, 77, 87]
     }
df = pd.DataFrame(d, index=['Mike', 'Kara', 'Lucy'])
print(df)

print('====Random initialization====')
df2 = pd.DataFrame(np.random.rand(3, 5), columns=list("ABCDE"))
print(df2)

# df3 = pd.DataFrame(np.random.randint(-30, 90, 15).reshape(3, 5)) # 2D numpy.ndarray
# print(df3.iloc[:, [0]])
# print(df3.iloc[:, [0]].diff(-1))

print('===index and columns===')
# the resulting index will be the union of the indexes of the various Series, the dict's key will be the columns
d = {
    "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
}
df4 = pd.DataFrame(d)
print(df4)
# index 行索引
print(df4.index)
# columns 列索引
print(df4.columns)
# df取一个columns的数据类型是什么？
# print(df4.one)

print('====row and column====')

'get a column'
# method1
print(df['Math'])
# method2
print(df[['Math', 'Chemistry']])
# method3
print(df.loc[:, ['Physics']])
# method4
print(df.iloc[:, [1]])
# method5
print(df2.B)

'get a row'
# method1
print(df.loc[['Mike', 'Kara']])
# method2
print(df.iloc[[0]])
# method3
# 切片取行必须是范围，切片取列
# df2[-1:]  df2[:][-1:]# 取最后一行
# df2[:1]  df2[:][:1]# 取第一行

# loc works on labels in the index
# iloc works on positions in the index


print('===from structured or record array===')
# np.zeros(shape, dtype=float, order='C') 返回一个给定形状和类型的用0填充的数组
# i:整数  f浮点数  a字符串
# this will return a ndarray
data = np.zeros((2,), dtype=[("A", "i4"), ("B", "f4"), ("C", "a10")])
data = [(1, 2.0, "Hello"), (2, 3.0, "World")]
print(data)
print(data[:1])  # 对data中的元素个数切片[(1, 2.0, 'Hello')]

# 给df添加index & columns
# 可以同时添加也可以分开添加，！columns
df5 = pd.DataFrame(data, index=('a1', 'a2'), columns=('b1', 'b2', 'b3'))
print(df5)

print('===from a list of dicts===')
# the new df's columns will union the key, one dict will be one index
# i could change the index and the columns, but it must be the right number
data2 = [{'m': 15, "n": 16, "f": 31}, {"f": 1, "y": 45, "r": 4, "u": 2}]
df6 = pd.DataFrame(data2, index=(1, 2))
df6.columns = ["A", "B", "C", "D", "E", 'F']
print(df6)

'===from a dict of tuples==='
data3 = [('a', 'b', 'c'), ('d', 'e', 'f'), ('d', 'g', 's')]
df7 = pd.DataFrame(data3, index=("row1", 'row2', 'row3'), columns=("col1", 'col2', 'col3'))
