# 课堂练习3
# 编写程序，实现一个单词反转游戏。
# 要求：
# 1.使用切片的相关知识实现一个用于接收反转后的单词的函数reverse_words(word)
# 2.使用 with open 和 pickle.dump 将原始的单词保存到文件中，文件名为word.pkl。
# 3.使用 try/except 进行检查，若存在保存的单词文件，则使用 with open 和 pickle.load 加载原始单词；
#   若出现 FileNotFoundError 错误，则提示用户输入一个单词。
# 4.在程序结束时，使用 with open 和 pickle.dump 将新生成的单词保存到文件中，覆盖原来的单词。
#
# 提示：
# 1. [::-1] 表示对序列进行逆向遍历
# 2. 'rb'：以二进制格式打开一个文件用于只读；'wb'：以二进制格式打开一个文件只用于写入
# 在下方编写你的代码
