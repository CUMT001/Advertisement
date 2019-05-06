import time


def GetNow():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


print(GetNow())
fh = open("E:/algo.qq.com_641013010_testa/testA/ad_static_feature.out", "r")
list = fh.readlines()
print(GetNow())
print(len(list))
for i in range(5):
    list[i].strip()
    element = list[i].split("\t")
    length = len(element)
    print(len(element))
    for j in element:
        print(j, end=" ")
    print()
