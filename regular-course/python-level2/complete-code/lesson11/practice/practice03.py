# 课堂练习三
# 已知用于存储个人信息的字典info，要求将字典中的三年级改为五年级并遍历该字典，将字典中的所有键值对输出在控制台上
# 提示：
# （1）使用for循环遍历字典
info = {'name': 'LiMing', 'age': '11', 'grade': '三年级', 'gender': '男'}
# 在下方编写你的代码
info['grade'] = '五年级'
for key in info:
    print(key, info[key])
