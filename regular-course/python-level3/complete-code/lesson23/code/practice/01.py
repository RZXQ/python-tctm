# 1. 定义函数reverse和参数s, 遍历s, 将取出的字符拼接成反转后的字符串reversed返回
def reverse(s):
    reversed = ''
    for i in s:
        reversed = i + reversed
    return reversed


# 2. 定义加密函数encrypt，传入待加密字母字符串text和偏移量shift参数，在其中：
def encrypt(text, shift):
    # 3. 将字符串中字母转换为大写字母
    text = text.upper()
    # 4. 初始化空字符串encrText存储加密文本
    encrText = ''
    # 5. 遍历text，在循环中直接将字母转为ASCII码，再加偏移量shift，得到新ASCII码c
    for i in text:
        c = ord(i) + shift
        # 6. 再将新ASCII码c转为字母，并拼接成加密文本
        encrText = encrText + chr(c)
    # 7. 调用reverse函数，反转加密后的文本并返回
    return reverse(encrText)


# 8. 定义解密函数decrypt，在其中调用encrypt函数，传入加密文本和相反的偏移量，并返回
def decrypt(encrText, shift):
    return encrypt(encrText, -shift)


# 9. 获取用户输入text
text = input('请输入要加密的文本：')
# 10. 调用encrypt函数，传入用户输入和偏移量2，获取加密后的文本encrText，并输出
encrText = encrypt(text, 2)
print('加密后的文本是：', encrText)
# 11. 对加密后的文本encrText进行解密，输出解密后的文本
print('解密后的文本是：', decrypt(encrText, 2))
