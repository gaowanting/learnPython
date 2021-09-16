import pandas as pd
import tushare as ts
import random
import time

pro = ts.pro_api()

while True:
    # 在上市公司中随机抽取股票一支股票代码
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code, name, area,industry,list_date')
    tic = random.choice(data["ts_code"])

    # 从2007年到2020年随机选取10年的数据
    start_time = "2000-01-01"
    end_time = "2010-01-01"
    timestamp_s = time.mktime(time.strptime(start_time, "%Y-%m-%d"))
    timestamp_e = time.mktime(time.strptime(end_time, "%Y-%m-%d"))
    chose_time = random.randint(timestamp_s, timestamp_e)

    selected_start_time = time.strftime("%Y-%m-%d", time.localtime(chose_time))
    selected_end_time = time.strftime("%Y-%m-%d", time.localtime(chose_time + 315532800))

    # data_tmp = pd.DataFrame()
    # print(data_tmp.empty)
    data_tmp = ts.pro_bar(ts_code=tic, adj='qfq',
                      start_date=selected_start_time, end_date=selected_end_time)

    if data_tmp is not None:
        print(f"the selected stock for training model is: {tic}\nHere is the information")
        print(data[data["ts_code"] == tic])
        print("the selected train data period is:")
        print(selected_start_time, '----', selected_end_time)
        print(data_tmp)
        break


# print(not None)
