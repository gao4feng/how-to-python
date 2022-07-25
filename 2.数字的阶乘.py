# 2.数字的阶乘
# 输入一个数，计算其阶乘
# 例：6！ = 6 * 5 * 4 * 3 * 2 * 1
# 知识点： 函数定义， while循环

# 定义一个计算阶乘的函数
def get_jiecheng(number):
    result = 1
    while number > 0:
        result *= number
        number -= 1
    return result

# 函数的调用
# 快捷键ctrl + d 复制当前行
print("jiecheng 6 = ", get_jiecheng(6))
print("jiecheng 3 = ", get_jiecheng(3))
print("jiecheng 100 = ", get_jiecheng(100))

# 输出为
# jiecheng 6 =  720
# jiecheng 3 =  6
# jiecheng 100 =  93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000

# 断点和debug