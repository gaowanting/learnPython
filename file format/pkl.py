import pprint, pickle
# pkl是一种常见的数据格式
pkl_file = open(r'/data_small.pkl', 'rb')

# data1 = pickle.load(pke_file)
# pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()
