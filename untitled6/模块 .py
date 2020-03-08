# 1. 计算圆面积
# math 模块中的 pi 属性是圆周率π
import math

# 圆面积公式 S = π * r * r
r = 20

# 计算半径为 r 的圆面积
S = math.pi * r * r
print(S)

# 2. 生成10个随机数，输出里面最大的数
import random

a = [random.randint(0, 100) for i in range(10)]
print(a)
print(max(a))


# 3. 将第六课（while循环）练习1的猜数字小游戏中的数字用一个1-100之间的随机数来改写，并在猜中后输出猜了几轮猜中答案
import random
num = random.randint(1, 100)
right = False
i = 0
while not right:
    answer = int(input('请猜1-100的整数:'))
    i += 1
    if answer < num:
        print('你的数字太小了.已经猜了%d次.' % i)
    if answer > num:
        print('太大了!.已经猜了%d次.' % i)
    if answer == num:
        print('对了')
        right = True
        print('猜了%d轮猜中答案.' % i)