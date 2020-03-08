# 1. if条件判断
money = 88

# 当 money 的值大于 100 时，输出 "rich"
# 否则，输出 "poor"

if money > 100:
    print("rich")
else:
    print('poor')

# 2. 逻辑判断
# 判断下面示例是否会输出 True 并亲自验证

# （a）//输出True
bingo = False
if bingo == False:
    print(True)
else:
    print(False)
# （b）//输出False
b = 3
if b - 3:
    print(True)
else:
    print(False)
# （c）//直接按回车,输出False, 输入任何内容为True
x = input('请输入内容')
if x:
    print(True)
else:
    print(False)
# （d）//输出False, True, False, True, False, True, False
a = True
b = not a  # 不记得not请回顾第二课
print(b)
print(not b)
print(a == b)
print(a != b)
print(a and b)
print(a or b)
print(1 < 2 and b == True)



# 3. BMI 计算器
# BMI 指数（即身体质量指数，简称体质指数又称体重，英文为Body Mass Index，简称BMI），是用体重公斤数除以身高米数平方得出的数字
#
# BMI < 18.5 体重偏轻 18.5 <= BMI < 24 体重正常 BMI >= 24 体重偏重 设计一个BMI计算器吧，看看自己体重是否正常。
#
# 输入：身高、体重值
#
# 输出：BMI 指数、是否正常

height = input('输入身高')
weight = input('输入体重')
BMI = float(weight)/float(height)**2
if BMI < 18.5:
    print('体重偏轻,你的指数为:' + str(BMI))
elif 18.5 <= BMI < 24:
    print('体重正常,你的指数为:' + str(BMI))
elif BMI >= 24:
    print('体重偏重,你的指数为:' + str(BMI))


