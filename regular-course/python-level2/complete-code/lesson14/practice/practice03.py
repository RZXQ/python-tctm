# 课堂练习三
# 已知列表scores，其中60,70,80是已排序的元素，编写程序将元素75排列到列表scores中正确的位置并将排好序的列表输出在控制台上
# 提示：
# （1）找到要排序的元素索引
# （2）判断当前元素是否比它前一个元素小
# （3）变量交换：a,b=b,a
scores = [60, 70, 80, 75, 90]
# 在下方编写你的代码
j = 3
if scores[j] < scores[j - 1]:
    scores[j], scores[j - 1] = scores[j - 1], scores[j]
print(scores)
