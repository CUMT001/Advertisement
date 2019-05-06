import pandas as pd
import numpy as np


dict_data = {}
with open("E:/algo.qq.com_641013010_testa/testA/ad_static_feature.out", "r") as fh:
    # 字典中的键列表，比如这里分别代表广告 id、创建时间、广告账户 id、商品id、商品类型、广告行业id、素材尺寸
    key_list = ['id', 'time', 'account', 'product', 'product_type', 'trade', 'size']
    # 获得每行的长度
    cnt = len(key_list)
    for line in fh:
        data = line.strip().split('\t')
        for i in range(cnt):
            if cnt ==len(data):
                dict_data.setdefault(key_list[i], []).append(data[i])
            else:
                dict_data.setdefault(key_list[i], []).append(np.NaN)

print(type(dict_data.keys()))
columnsname = list(dict_data.keys())
frame = pd.DataFrame(dict_data, columns=columnsname)
frame.to_csv('file_out_asf.csv', index=False, header=False)
