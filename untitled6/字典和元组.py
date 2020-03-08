# 字典
# 创建一个字典，包含 one、two、three 三个键
# 对应的值分别为 1，2，3
data = {'one': 1,
        'two': 2,
        'three': 3
        }

# 将 two 键对应的值改为 4
data['two'] = 4
print(data)

# 统计下这段文字里，不同单词出现的次数
s = 'Beautiful is better than ugly Explicit is better than implicit Simple is better than complex Complex is better ' \
    'than complicated Flat is better than nested Sparse is be '
list_s = s.split()
set_s = set(list_s)
# print(list_s)
# print(set_s)
# n = 0
# for i in set_s:
#     print(list_s.count(i))
#     n += list_s.count(i)
#     print(n)
# print(len(list_s))
data = {i: list_s.count(i) for i in set_s}
print(data)
