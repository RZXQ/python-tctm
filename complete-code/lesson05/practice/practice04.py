# 课堂练习四
# 请按照要求，编写一个 “石头剪刀布”的程序（默认电脑出 “石头” ）
# 提示：1. 在无限循环中，通过input()指令输入自己要出的手势
#      2. 如果输入的手势是“石头”，就输出“平局！请重新输入”
#      3. 如果输入的手势是“剪刀”，就输出“失败！请重新输入”
#      4. 如果输入的手势是“布”，就输出“胜利”，并结束循环


print('**石头剪刀布**')
print('**预备~开始!**')

# 请在下方编写石头剪刀布的代码
while True:
    gesture = input("请输入你的手势：")
    if gesture == '石头':
        print('平局！请重新输入')
    if gesture == '剪刀':
        print('失败！请重新输入')
    if gesture == '布':
        print('胜利！')
        break
