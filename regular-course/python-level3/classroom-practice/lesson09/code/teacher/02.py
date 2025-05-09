'''
我用Pyqt5库中的类创建了一个计算器应用程序窗口
问题：我想在这个窗口中创建很多按钮，如何批量创建
解决：今后凡事遇到横竖规律分步的多个相同控件，都可用数据和界面分离的方式批量创建
1.先定义二维数组来存储按钮文本
2.使用双层for循环遍历二维数组创建按钮显示文本
3.将按钮添加到布局中

这是我的授课代码：
btns = [
    ['7', '8', '9', '+'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '*'],
    ['.', '0', '=', '/'],
    ['c'],
]
for r in range(len(btns)):
    row = btns[r]
    for c in range(len(row)):
        btn = QPushButton(btns[r][c])
        layout.addWidget(btn, r+1, c)

请帮我使用中文，根据以上内容出5道单选题，帮助学员理解批量创建控件不需要答案。
'''
