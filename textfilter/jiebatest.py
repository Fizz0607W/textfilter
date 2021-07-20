import jieba

with open ("keywords") as f:
    keyword = f.readlines()

for kw in keyword:

    seg_list = jieba.lcut(kw, cut_all=False, HMM=True)
    print(seg_list," ",kw)  # 默认模式