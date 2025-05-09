'''
在即时通信项目中要实现视频聊天，现在部分功能的讲解步骤是这样的：
问题：视频聊天如何发起？
解决：需要先有一个启动按钮，点击按钮开始视频聊天
问题：如何设置视频聊天按钮
解决：1.创建按钮控件，设置大小，边框；2.为按钮设置显示图标；3.设置按钮位置；4.设置点击事件绑定
但是视频聊天按钮上来就显示，并不合理，所以先将按钮设置为隐藏，然后选择好友，且好友不是自己时显示。
问题： 是不是点击视频聊天按钮就直接启动摄像头，进行视频聊天
分析：视频聊天最简单流程 1.  一方主动发起聊天请求，服务端把请求转发给对方；2. 另一方同意视频聊天请求，
才建立连接；3. 连接成功，才能进行视频聊天。
问题：现在服务端回复的视频聊天确认消息，就可以打开视频聊天窗口，如何打开？
分2步骤： 1. 创建视频窗口类
* 按照我们创建窗口的习惯，会为每个子窗口定义专门的类，并继承QWidget，所以定义VideoWindow类，包含视
频聊天窗口的所有内容
* 因为将来在视频通信中也需要明确聊天的双方，所以初始化方法中传入通信双方名字，就是sender和to
* 给窗口设置标题和大小：视频窗口如果挡着窗口不方便，让视频窗口出来时放在左上角，使用setGeometry方法既能设
置位置，也能设置大小
* 将来视频窗口也需要放控件，所以先准备一个空的layout布局备用
* 我们希望创建窗口对象时就自动显示窗口 self.show()
2. 在content是call时，创建视频通信窗口类对象，传入sender和to
问题：视频通信功能怎么做，如果从0开始完成一个视频聊天项目，需要学习很多很多知识
解决：在真实的软件公司中，开发一个庞大的复杂的程序，有时为了缩短研发周期，降低开发难度也会借助一些开源软件
问题：什么是开源？
讲解：其实开源就是开放源代码的意思。简单说就是很厉害的人或公司把代码研发出来，免费给大家使用。
比如我们这次使用的开源程序是是： 网络视频语音实时通信程序就是专门实现网络视频通信功能的软件
问题： 要如何使用这个程序呢？
解答： 这个程序也包含客户端和服务端两部分：服务端老师已经部署在公共的服务器上了，客户端需要通过浏览器访问
网址使用：1. 同学们打开浏览器，在地址栏输入网址 2. 打开网址后，将自己的组名添加到“房间名”后的文本框中
3. 点击“连接到在线房间”，连接到在线的房间。4.另一个同学使用相同的组名，相同的操作步骤，也连接到相同的房间。
问题： 可是我们是用的pyqt创建的视频聊天窗口，现在视频通信用的是浏览器网页，不是我们的窗口啊
解决：pyqt提供了专门的QWebEngineView控件可以再pyqt窗口中显示网页，就像一个缩小版的浏览器，只不过没有地址栏
1. 创建浏览器控件；2.浏览器控件中添加要显示的网页地址；3.将浏览器控件添加到布局中

我的这部分的核心代码：
class VideoWindow(QWidget):
    def __init__(self, sender, to):
        super().__init__()
        self.sender = sender
        self.to = to
        self.setWindowTitle('Video')
        self.setGeometry(0, 0, 660, 340)
        layout = QGridLayout()
        self.setLayout(layout)
        self.show()
        # 1. 创建浏览器控件
        self.browser = QWebEngineView()
        # 2. 浏览器控件设置当前显示的网页为https://l345.61it.cn/python.html
        self.browser.setUrl(QUrl('https://l345.61it.cn/python.html'))
        # 3. 浏览器控件添加到布局中
        layout.addWidget(self.browser)

    class ChatWindow(QWidget):
      ...
      def handle(self, msg):
         ...
         # 1.判断是否为视频聊天消息
         elif msg['cmd'] == 'video':
            content = msg['content']
            if content == 'call':
                # 3.播放摄像头捕获视频
                global videoWindow
                videoWindow = VideoWindow(msg['sender'], msg['to'])


请根据以上内容帮我使用中文，根据以上知识点出5道单选题，主要考察：如何设置视频聊天按钮，最简单视频聊天过程，
什么是开源程序，widget窗口设置出现位置，如何在窗口中显示网页内容等知识，不需要答案.

'''
