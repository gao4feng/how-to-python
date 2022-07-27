# 14.统计英语文章中每个单词的出现次数
# 输入文件：一篇英文文章
# 输出

word_count = {}

with open("./beginner_guide_to_python.txt") as fin:
    for line in fin:
        line = line[:-1]
        words = line.split()
        for word in words:
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1

print(
    sorted(
        word_count.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]
)
# 输出结果
# [('Python', 45), ('to', 35), ('the', 33), ('a', 28), ('you', 26), ('and', 24), ('of', 21), ('for', 19), ('your', 16), ('can', 10)]




