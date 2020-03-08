# 1. 字符串拼接
name = 'Crossin'
age = 18
code = 'Python'

# 通过 % 将 name, age, code 拼接成一句话
# 输出 Crossin is 18, he writes Python.
result = '%s is %d, he writes %s.' % (name, age, code)
print(result)


# 2. print()
num1 = '3.3'
num2 = 2.5

# 将 num1 转换为浮点数
num1 = float(num1)

# 再和 num2 相加后输出
print(num1 + num2)

# 3. bool类型转换
# 判断以下结果的值为 True 还是 False：
print(bool(-123) == True)
print(bool(0) == False)
print(bool('abc') == True)
print(bool('False') == True)
print(bool('') == False)
print(bool([]) == False)
print(bool({}) == False)
print(bool(['']) == True)
print(bool(None) == False)
