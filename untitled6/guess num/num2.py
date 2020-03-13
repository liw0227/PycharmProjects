import random


def File():
    f = open("game_one_user.txt")
    data = f.read().split()
    f.close()
    if not data:
        data = ['0', '0', '99', '0']  # 默认值
    return [data[0], data[1], data[2], data[3]]


def GuessNumber():
    name = input('请输入你的名字')
    file = File()
    print(file)
    if name in file:
        print(f'{file[0]}欢迎回来，你的最佳历史数据是：玩了{file[1]}次，最少{file[2]}次猜出答案。平均{file[3]}次猜出答案。')
    else:
        print('欢迎你首次来玩游戏。')
    counts = []
    r = 1
    while True:
        ans = random.randint(1, 100)
        print(ans)
        count = 0
        while True:
            guess = input('请输入1-100的整数。')
            count += 1
            try:
                if 1 <= int(guess) <= 100:
                    if int(guess) > ans:
                        print(f'你输入的数值{guess}比答案大了，请再次输入。')
                    elif int(guess) < ans:
                        print(f'你输入的数值{guess}比答案少了，请再次输入。')
                    else:
                        print(f'你输入的数值{guess}答案正确。你猜了{count}次。')
                        counts.append(count)
                        break
                else:
                    print(f'{name}你的输入的数值{guess}不在1-100,请再输入。')
            except:
                print(f'{name}你输入的是{guess},数据有误。请再输入。')
        r += 1
        f = sum(counts) / len(counts)
        y = input(f'{name}现在第{r - 1}轮结束，暂时最少{min(counts)}次猜出答案，暂时平均{("%.2f" % f)}次猜出答案。你还要玩吗？继续请按"y",按其它键退出。')
        if y != 'y':
            print(f'{name}你玩了{r - 1}轮，累计最少{min(counts)}次猜出答案，累计平均{("%.2f" % f)}次猜出答案。退出游戏，欢迎下次再来。')
            break
        else:
            print(f'--------------现在进行:第{r}轮-------------------')
    avg = "%.2f" % f
    if int(file[2]) > min(counts):
        with open('game_one_user.txt', 'w') as f:
            data = f'{name} {r - 1} {min(counts)} {avg}'
            f.write(data)
    else:
        print('你的成绩还没上次好，本次成绩不作记录。')


GuessNumber()
