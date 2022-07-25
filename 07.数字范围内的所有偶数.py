# 6.数字范围中的所有偶数
# 返回列表
# 输入begin=4, end = 15
# 返回[4, 6, 8, 10, 12, 14]

def get_even_numbers(begin, end):
    result = []
    for item in range(begin, end):
        if item % 2 == 0:
            # 列表操作,添加元素
            result.append(item)
    return result


begin = 4
end = 15
print(f"begin={begin}, end={end}, even numbers:", get_even_numbers(begin, end))

# 等效操作
data = [item for item in range(begin, end) if (item % 2) == 0]
print(f"begin={begin}, end={end}, even numbers:", data)

# 输出为
# begin=4, end=15, even numbers: [4, 6, 8, 10, 12, 14]
# begin=4, end=15, even numbers: [4, 6, 8, 10, 12, 14]
