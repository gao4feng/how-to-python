# 3.打印区间内的所有素数


# 分两步进行
# 1. 判断一个数是否为素数
# 2. 遍历区间，打印所有的素数

# 判断是否为素数
def is_prime(number):
    # if语句， for循环
    if number in (1, 2):
        return True
    for idx in range(2, number):
        if number % idx == 0:
            return False
    return True

def print_primes(begin, end):
    # for循环,range用法（返回输入的范围内的数字，不包括右边界，所以+1）
    for number in range(begin, end+1):
        if is_prime(number):
            print(f"{number} is a prime")

begin = 11
end = 25
print_primes(begin, end)

# 输出为
# 11 is a prime
# 13 is a prime
# 17 is a prime
# 19 is a prime
# 23 is a prime