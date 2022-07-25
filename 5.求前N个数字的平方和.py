# 5.求前N个数字的平方和

def sum_of_square(n):
    result = 0
    for number in range(1, n+1):
        result += number * number
    return result

print("sum of square 3: ", sum_of_square(3))
print("sum of square 5: ", sum_of_square(5))
print("sum of square 10: ", sum_of_square(10))


# 输出为
# sum of square 3:  14
# sum of square 5:  55
# sum of square 10:  385