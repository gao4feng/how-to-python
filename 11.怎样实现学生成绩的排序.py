# 11.怎样实现学生成绩的排序
students = [
    {"sno": 101, "sname": "小张", "sgrade": 88},
    {"sno": 102, "sname": "小王", "sgrade": 99},
    {"sno": 103, "sname": "小李", "sgrade": 77},
    {"sno": 104, "sname": "小赵", "sgrade": 66},
]

# lambda函数，快速函数
students_sort = sorted(students, key=lambda x: x["sgrade"])

print(students)
print(students_sort)
# 输出为
# [{'sno': 101, 'sname': '小张', 'sgrade': 88}, {'sno': 102, 'sname': '小王', 'sgrade': 99}, {'sno': 103, 'sname': '小李', 'sgrade': 77}, {'sno': 104, 'sname': '小赵', 'sgrade': 66}]
# [{'sno': 104, 'sname': '小赵', 'sgrade': 66}, {'sno': 103, 'sname': '小李', 'sgrade': 77}, {'sno': 101, 'sname': '小张', 'sgrade': 88}, {'sno': 102, 'sname': '小王', 'sgrade': 99}]
