# 8.移除列表中的多个元素
# 输入原始列表[3, 5, 7, 9, 11, 13], 移除元素[7, 11]
# 返回[3, 5, 9, 13]
def remove_elements_from_list(lista, listb):
    for item in listb:
        lista.remove(item)
    return lista


lista = [3, 5, 7, 9, 11]
listb = [7, 11]
print(f"from {lista} remove {listb}, result: ", remove_elements_from_list(lista, listb))

# 等效操作
lista = [3, 5, 7, 9, 11]
listb = [7, 11]
data = [item for item in lista if item not in listb]
print(f"from {lista} remove {listb}, result: ", data)
# 输出为
# from [3, 5, 7, 9, 11] remove [7, 11], result:  [3, 5, 9]
# from [3, 5, 7, 9, 11] remove [7, 11], result:  [3, 5, 9]
