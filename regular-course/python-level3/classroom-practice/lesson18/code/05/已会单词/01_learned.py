'''

帮我生成一个pyqt窗口，整个窗口的大小为1200*675，窗口标题为'已会单词'
为窗口创建布局，并在布局中添加一个0行2列的表格，然后将布局添加到窗口中
设置表格的表头为['单词'，'中文释义']
使用QHeaderView.Stretch拉伸表头让表格占满窗口
使用utf8编码方式打开data.csv,
如果数据第三列是已会，就读取前面的单词和释义，将单词和释义分别写入表格的单元格
为每行代码添加注释

'''
