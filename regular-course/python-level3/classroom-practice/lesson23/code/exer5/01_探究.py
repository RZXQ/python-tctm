'''
第一段提示词：

我在pyqt按钮单击事件处理函数中，执行了res = socket.recv(1024).decode()
和res=json.loads(res)。可是现在服务端返回的信息超过1024字节。
导致我点击按钮执行这两句话时，界面直接自动退出，而且pycharm控制台还不报任何错误！
我想问：这段程序为什么会自动退出？可能发生了什么错误？如何验证是否发生了哪种错误？

'''

'''
第二段提示词：

以前程序运行出错，都会在控制台报错，但是咱在pyqt的按钮单击事件处理函数中程序出错，竟然不报错，
程序直接自动退出？这是为什么？如何让程序把真正的错误原因报出来？

'''
