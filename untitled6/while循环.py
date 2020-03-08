# 猜数字小游戏
# 在第四课里，我们用 if 改进猜数字小游戏后，功能已经基本实现了。但是有没有办法能让玩家一直猜，直到猜中为止？试着用 while 循环完成这个任务
import random
num = random.randint(1, 10)
right = False
while not right:
    answer = int(input('请猜1-10的整数:'))
    if answer < num:
        print('你的数字太小了.')
    if answer > num:
        print('太大了!')
    if answer == num:
        print('对了')
        right = True

# while, continue
# 输出 1 到 10，但不输出 4 和 5
count = 0
while count < 10:
    count += 1
    if count in [4, 5]:
        continue
    print(count)

# 使用 while 计算100以内所有3的倍数的和（即：计算3、6、9 ... 96、99 的和）
a = 0
i = 0
while i < 100:
    a += i
    i += 3
print(a)