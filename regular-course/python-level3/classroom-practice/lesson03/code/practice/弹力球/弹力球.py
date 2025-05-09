"""

请使用pygame制作一个弹力球游戏，我已经在images文件夹中准备了如下资源：
1. 游戏背景图bg.png
2. 弹力球图片ball.png
3. 砖块图片brick.png
4. 挡板图片baffle.png

我希望你使用面向对象的方式实现如下功能

1. 游戏窗口大小为（480,650），游戏帧率为60，在主循环中绘制背景，
2. 游戏得分初始为0，并绘制在10,10位置，文字颜色为黑色，它是全局变量
2. 绘制一个挡板，y坐标为600，x坐标为鼠标的x坐标，它的长度为100，
3. 绘制一个弹力球，初始位置在挡板上方，初始垂直移动方向向上，水平移动方向随机，水平和垂直移动速度为5，
5. 绘制5行8列个砖块，从坐标为(85, 100)的位置开始，并且他们上下左右之间的间隔为10
6. 当弹力球碰到挡板或者窗口左、右、上边界时反弹，碰到窗口下边界时游戏结束
7. 当弹力球碰到砖块时砖块就会消失，弹力球反弹，并且游戏得分加一

请只输出符合要求的代码块，且一定要在代码中添加每行注释

"""
