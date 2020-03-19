# 画出下列代码内存图

list01 = [
    1, 2, 3,
    [4, 5, 6]
]
# 将变量list01存储的地址赋值给变量list02
list02 = list01
# 将列表浅拷贝（创建新列表）一份赋值给变量list02
list03 = list01[::]
# 将右侧数据地址赋值给列表第一个元素
list02[0] = [7, 8, 9]
# 遍历右侧数据将每个元素赋值给左侧元素
list03[0:1] = [9, 10, 11]
# 　修改列表最后一个元素的第一个元素
list03[-1][0] = "悟空"
print(list01)
print(list02)
print(list03)