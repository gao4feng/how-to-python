# 10.怎样对简单列表元素进行排序
# 什么是简单列表
# 元素不是复合类型的列表（列表\元素\字典）
# 例1：[20, 50, 10, 40, 30]
# 例2：['bb', 'ee', 'aa', 'dd', 'cc']

lista = [20, 40, 30, 50, 10]
# 原地牌序（lista被改变)
lista.sort()
print(f"lista is {lista}")

lista = [20, 40, 30, 50, 10]
listb = sorted(lista)
print(f"lista is {lista}")
print(f"listb is {listb}")
# 输出为
# lista is [10, 20, 30, 40, 50]
# lista is [20, 40, 30, 50, 10]
# listb is [10, 20, 30, 40, 50]
