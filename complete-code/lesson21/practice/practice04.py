# 课堂练习四
# 现在需要在农场的土地中种植植物，已知农场有6块土地，第1块土地种植1株植物，第2块土地种植3株植物，第3块土地种植9株植物，以此类推，每块土地种植的植物株数是前一块土地的3倍
# 编写代码，在控制台输出每块土地需要种植的植物数量并计算总共需要种植多少株植物
n = 1
sum = 0
for i in range(1, 7):
    print('第', i, '块土地种植', n, '株植物')
    sum += n
    n *= 3
print('农场一共种植了', sum, '株植物')