# 函数
# 1. 思考下面这段程序会输出什么并亲自试一试
def func(x):
    print(x)  # 控制台打印x传入的变量.
    return x + 1  # 返回一个x+1


x = 2
print(func(x))
'''控制台打印:  2   //由def func(x):
                          print(x) 得到打印 2  
               3   //由def func(x)返回一个x+1 
                    print(x+1) 得到打印 3'''


# 2. 创建函数
# 创建一个函数 func，有一个参数 param
# 将输入参数的数值乘以2，作为返回值

def func(param):
    return param * 2


p = func(20)
print(p)


# 3. 实现一个函数，输入参数是两个列表，输出返回值是两个列表元素合并并排序后的结果，比如
# combine([1,5,3], [2,6,7,4])
# 返回结果
# [1,2,3,4,5,6,7]

def combine(list1, list2):
    print(sorted(list1 + list2))


combine([1, 5, 3], [2, 6, 7, 4])
