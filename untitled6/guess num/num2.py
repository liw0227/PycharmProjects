import random

name = input('请输入你的名字')
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
        print(f'--------------现在进行，第{r}轮-------------------')
avg = "%.2f" % f
with open('game_one_user.txt', 'a') as f:
    data = f'------我是分界线，{name}玩家数据------\n玩家:{name} \n玩了多少轮：{r-1} \n最少几次猜出答案：{min(counts)} \n平均几次猜出答案：{avg}\n'
    f.write(data)
