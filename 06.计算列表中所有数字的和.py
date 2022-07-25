# 6.计算列表中所有数字的和

def sum_of_list(param_list):
    total = 0
    for item in param_list:
        total += item
    return total


# 格式化代码 ctrl+alt+l
# 列表
list_1 = [1, 2, 3, 4]
list_2 = [17, 5, 3, 5]

print(f"sum of {list_1}, ", sum_of_list(list_1))
print(f"sum of {list_2}, ", sum_of_list(list_2))

# python本身也有sum函数
print(f"sum of {list_1}, ", sum(list_1))
print(f"sum of {list_2}, ", sum(list_2))


# 输出为
# sum of [1, 2, 3, 4],  10
# sum of [17, 5, 3, 5],  30
# sum of [1, 2, 3, 4],  10
# sum of [17, 5, 3, 5],  30
