# 课堂练习4
# 已知班级中所有人的姓名列表name，还有在与人名对应的成绩列表score。请将两个列表合并成一个字典，使字典中的人名与其成绩可以一一对应。

# 提示1：dict.fromkeys()函数中，填入列表，可以生成一个只有键的字典。
# 提示2：通过循环遍历上面的字典，可以依次给所有的键进行赋值。

name = ['小明', '小红', '小刚', '小李', '小张']
score = [98, 85, 92, 88, 94]

scores = dict.fromkeys(name)
i = 0
for k in name:
    scores[k] = score[i]
    i = i + 1
print(scores)
