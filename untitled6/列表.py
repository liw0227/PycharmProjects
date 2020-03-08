# 1. 操作列表
# 创建一个列表 lst，其中的元素依次是 1，2，3
lst = [1, 2, 3]

# 输出 lst 中的第一个元素 1
print(lst[0])

# 将 lst 的第二个元素 2 改为 4

lst[1] = 4
print(lst)
# 在 lst 末尾再增加一个元素 5

lst.append(5)
print(lst)

# 2. 列表切片操作
lst = [365, 'everyday', 0.618, True, 2, 5]

# 取出 lst 的第二个位置至倒数第二个位置的子
lst = lst[1:-1]
# 创建为一个新列表 lst2
lst2 = lst
print(lst2)

# 分割与连接字符串
word = 'I am Mr Crossin of Python'

# 将字符串 word 按照空格分割成一个列表
lst = word.split()
print(lst)

# 再将分割后的列表以逗号(,)重新拼接成字符串
word = ','.join(lst)
print(word)