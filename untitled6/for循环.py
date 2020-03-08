# 计算100以内所有3的倍数的和（即：计算3、6、9 ... 96、99 的和）
count = 0
for i in range(1, 101):
    if i % 3 == 0:
        count += i
print(count)

print(sum(range(3, 100, 3)))


# 2. 分别输入高和宽两个整数，输出对应高度和宽度的矩形。比如：
# 输入3和4，输出
#
# * * * *
# * * * *
# * * * *
# 输入5和7，输出
#
# * * * * * * *
# * * * * * * *
# * * * * * * *
# * * * * * * *
# * * * * * * *
def num(height, weight):
    for i in range(height):
        print('* ' * weight)


num(3, 4)
num(5, 7)

# 3. 输出九九乘法口诀表
# 1 x 1 = 1
# 1 x 2 = 2
# ...
# 9 x 1 = 9
# ...
# 9 x 9 = 81

for i in range(1, 10):
    for j in range(1, 10):
        print('%d x %d = %d' % (int(i), int(j), int(i * j)))

# 4. 跳出循环
nums = [23, 45, 8, 13, 50, 43, 21]

# 把 nums 里的值从前向后累加
# 当总和超过 100 时则不再继续累加

sum = 0
for n in nums:
    # 累加
    sum += n

    if sum > 100:
        break
# 满足条件时跳出循环


print(sum)