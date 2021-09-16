import numpy as np

# do Matrix multiplication by numpy

# 步骤1: Numpy数组
# arange(9)表示生成从0到9的序列reshape(3, 3)表示将这个序列重新设置成3行3列的矩阵
A = np.arange(9).reshape(3, 3)
B = np.arange(10, 19).reshape(3, 3)
print('A:{}'.format(A))
print('B:{}'.format(B))

# 步骤2: dot 方法
result = A.dot(B)
print(result)

# random
# 通过本函数可以返回一个或一组服从标准正态分布的随机样本值 N（0，1）参数为返回的形状
np.random.randn(6, 4)
# 返回一个或一组服从“0~1”均匀分布的随机样本值。随机样本取值范围是[0,1)，不包括1
np.random.rand()
