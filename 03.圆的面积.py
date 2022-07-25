# 3.圆的面积
# 输入半径，计算圆的面积

# 知识点 库的使用
# 从math库中使用pi（圆周率）
import math
#print(math.pi)

def compute_area_of_circle(r):
    # round函数，保留有效位
    return round(math.pi * r * r, 2)

print(" area of 2 is:", compute_area_of_circle(2))
print(" area of 3.14 is:", compute_area_of_circle(3.14))
print(" area of 6.78 is:", compute_area_of_circle(6.78))

# 输出为
#  area of 2 is: 12.57
#  area of 3.14 is: 30.97
#  area of 6.78 is: 144.41
