# 课堂练习二
# 已知列表nums记录了一些整数
# 要求：请使用列表推导式构建一个新列表，其中包含nums中所有大于0的偶数
# 示例：[2, 4, 6, 8]

nums = [-1, 3, 0, 2, -4, 4, 7, 9, 6, 8, -2, 5]
# 请在下方编写代码
new_list = [num for num in nums if num > 0 and num % 2 == 0]
print(new_list)
