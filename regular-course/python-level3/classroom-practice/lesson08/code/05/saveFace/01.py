'''

我想使用deepface完成人脸信息识别保存。创建Recognize类包含两个函数作为静态方法。
一个方法recognize_face负责使用deepface模块的represent进行人脸识别，将图像信息识别后，用numpy转换为数组，返回人脸数组数据，如果没有识别到人脸可以返回None，添加try避免未识别到人脸报错
另一个方法store_face负责传入人名和要识别的人脸图像，调用第一个函数功能，将人名和对应图像转换后的数组数据用csv.writer方法写入data.csv文件，写做一行，将来用于对比
请帮我生成代码，并添加一定的中文注释和解释。测试时可以使用face文件夹下的xiaolong1.jpg 图片，名字叫小龙

追问 ：
我发现recognize_face函数的返回值太复杂了，识别结果是一个列表，列表第一项是一个字典,
我只需要这个字典中embedding的值转换为数组返回就可以。请为我稍微修改下recognize_face函数

'''
