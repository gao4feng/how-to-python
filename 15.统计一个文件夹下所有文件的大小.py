# 15.统计一个文件夹下所有文件的大小

import os
print(os.path.getsize("beginner_guide_to_python.txt"))


sum_size = 0
for file in os.listdir("."):
    # 判断是否是文件而不是文件夹
    if os.path.isfile(file):
        # print(file)
        sum_size += os.path.getsize(file)

print("all size of dir:", sum_size/1000)
# 输出结果
# 6485
# all size of dir: 7.044


