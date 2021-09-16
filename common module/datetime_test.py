import datetime
import numpy as np

np.random.seed(1)
date_cn = []
date_en = []
for timestamp in np.random.randint(143835585, 2043835585, 10):  # 返回在给定范围内的10个时间戳
    date = datetime.datetime.fromtimestamp(timestamp) # 从时间戳转换成日期格式
    date_cn.append(date.strftime("%y-%m-%d"))
    date_en.append(date.strftime("%d/%b/%Y"))
    print(date)
print(date_cn)
print(date_en)

# 日期的格式转化
'''
    date 2033-06-06 15:21:45
    date.strftime("%y-%m-%d") 进行日期转化
    %y %Y 两位数年份  四位数年份
    %m  %M 月  分钟
    %d  %b 日期 英文月份
'''

# 获取当天数据
print(type(datetime.date.today()))
print(type(datetime.date.today().strftime("%Y%m%d")))
