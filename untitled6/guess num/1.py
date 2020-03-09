# 提示用户猜一个数字，把 用户输入的数字A 与 一个程序随机生成的数字B 进行比较，提示 数字A 大于/小于/等于 数字B。用户可以反复猜 数字B，直到猜中为止
import random


def number():
    count = 0
    right = False
    while not right:
        a = input('请输入一个1-100的整数.')
        count += 1
        try:
            if int(a) < 0:
                print('你输入的是一个负数.')
            elif int(a) > 100:
                print('你输入的数字大于100了.')
            else:
                right = True
                return [int(a), count]

        except:
            print('请确实输入的是0-100整数')


def main():
    num = random.randint(1, 100)
    print(num)
    bingo = False
    i = 0
    while not bingo:
        lis = number()
        a = lis[0]
        i += lis[1]
        if num > a:
            print('你的数字太少了.')
        elif num < a:
            print('你的数字太大了!')
        elif num == a:
            print(f'你猜对了,猜了{i}次')
            bingo = True


def time():
    main()
    count = 0
    while True:
        count += 1
        a = input('如果继续按"y",其它键退出.')
        if a == 'y':
            main()
        else:
            print(f'你玩了{count}次.')
            break


if __name__ == '__main__':
    time()
