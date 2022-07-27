# 9.怎样对列表元素去重
# 输入原始列表（带有重复元素）[10, 20, 30, 10, 20]
# 返回[10, 20, 30]
def get_unique_list(lista):
    result = []
    for item in lista:
        if item not in result:
            result.append(item)
    return result


lista = [10, 20, 30, 10, 20]
print(f"source list {lista}, unique list:", get_unique_list(lista))

# 等效做法
# set函数转化为集合，集合有唯一性，再转化为list
print(f"source list {lista}, unique list:", list(set(lista)))
# 输出为
# from [3, 5, 7, 9, 11] remove [7, 11], result:  [3, 5, 9]
# from [3, 5, 7, 9, 11] remove [7, 11], result:  [3, 5, 9]
