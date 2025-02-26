'''

这是我的授课思路：
程序中，通常什么时候显示右键菜单？
通常在表格中点击鼠标右键时显示右键菜单
怎么知道点了鼠标右键？
事件绑定，但不是clicked，clicked只表示左键点击，
因为绝大多数情况下，点击右键都是为了显示右键菜单，
所以，有一个专门的事件customContextMenuRequested
当（你点击了鼠标右键）想要显示自定义菜单时，就触发
为什么关联事件后点击右键没反应？
还需要修改设置，启用自定义的右键菜单
self.table.setContextMenuPolicy(Qt.CustomContextMenu)
创建和使用自定义右键菜单正确的顺序是什么？
先创建菜单QMenu()
然后添加一个或多个选项QAction()，每个选项可以通过triggered关联事件处理函数

请使用中文根据以上内容出5道单选题，帮助学员理解如何在PyQt程序中使用右键菜单，不需要答案和解析。

'''
