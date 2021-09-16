# 在列表中使用for in\ if else
l = [x for x in range(10, 20)]
l2 = [y**2 for y in l if y>15]

print(l2)

print([0]*3)
# [0,0,0]
# list * n -> 列表变成n倍长度

#  l:[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
l.pop()  #  pop()默认为剔除最后一项，并返回pop出来的值