# 课堂练习1
# 使用if语句模拟手机在电量小于百分之二十时，就发出“电量低”的提醒功能，假设初始电量为10%
# 提示1：百分之二十的大小为0.2
# 提示2：电量可用power表示
# power = 0.1
# if power < 0.2:
#     print('电量低')

power = float(input())

if power < 0.2:
    print('电量低')
else:
    print('电量高')
