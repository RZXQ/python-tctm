# 课堂练习1
# 编写代码，实现根据输入的西瓜重量为西瓜大小分类的程序效果，当西瓜重量大于10时，在控制台输出'大西瓜'；
# 当西瓜重量大于5时，在控制台输出'中等西瓜'；当西瓜重量大于0时，在控制台输出'小西瓜'；否则在控制台输出'输入错误'
# 提示：
# 使用input()实现输入框功能
# 使用if-elif-else语句实现判断西瓜重量
# 在下方书写代码
weight = input("请输入西瓜的重量：")
weight = int(weight)
if weight > 10:
    print('大西瓜')
elif weight > 5:
    print('中等西瓜')
elif weight > 0:
    print('小西瓜')
else:
    print('输入错误')
