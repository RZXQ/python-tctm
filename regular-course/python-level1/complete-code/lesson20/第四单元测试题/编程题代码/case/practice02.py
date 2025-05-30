# 编写代码，将在控制台输入的任意内容保存在text.txt文件中。
# 要求：
# （1）使用with open()在文件中写入内容
# （2）以只写模式 “w”打开文件
# （3）text.txt文件的位置：在与编写代码的py文件同级的files文件夹中
# 提示：
# （1）设置编码方式为encoding='utf-8'
# （2）在文件中写入内容的函数是write()
content = input('请输入要保存的内容：')
with open('files/text.txt', 'w', encoding='utf-8') as f:
    f.write(content)
