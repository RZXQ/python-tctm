# 课堂练习四
# 已知字典menu用于存储菜品和价格，要求编写代码，定义一个函数来修改或添加字典中的键值对
# 最后将修改完的menu字典输出在控制台上
# 提示：
# （1）在定义的函数中传入三个参数，分别是键、值以及menu字典
# （2）使用if-else语句判断传入的键是否存在于menu字典中（if key in menu:），如果存在，就提示该菜品已存在
#  如果不存在传入的键，就使用"字典名[键]=值"的方式为该字典添加一个新的键值对
# （3）函数的最后使用return关键字返回menu字典
# （4）调用函数并将修改后的字典输出在控制台上
# 预留代码
menu = {'鱼香肉丝': 12, '宫保鸡丁': 10, '地三鲜': 10}


# 在下方编写你的代码
# 定义一个函数来修改或添加字典中的键值对
def modify_dict(key, value, menu):
    if key in menu:
        print('该菜品已存在')
    else:
        menu[key] = value
    return menu


# 调用函数
print(modify_dict('鱼香肉丝', '5元', menu))
print(modify_dict('番茄鸡蛋', '5元', menu))
