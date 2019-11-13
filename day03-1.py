"""
day03----循环结构
"""
"""
用for循环实现1~100求和
Version: 01
Author: zyayu
"""
sumx = 0
for x in range(101):  # 等同于 for x《 101  range(101)可以产生一个0到100的整数序列。
    sumx += x  # range(1, 100)可以产生一个1到99的整数序列。
print(sumx)  # range(1, 100, 2)可以产生一个1到99的奇数序列，其中2是步长，即数值序列的增量
sumy = 0
for i in range(1, 101, 2):
    sumy += i
print(sumy)
"""
While 循环
"""
"""
猜数字游戏
计算机出一个1~30之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了,充值 继续？？

Version: 0.1
Author: zyayu
"""
import random

amswer = random.randint(1, 30)
counter = 0
guesstime = 0

while counter <= 2:
    counter += 1
    guesstime += 1
    print("请猜一个0-30的数字,你一共有%d次机会: " % (4-counter))
    numberguess = int(input())
    if numberguess > amswer:
        print("请猜小一点")
    elif numberguess < amswer:
        print("请猜大一点")
    else:
        print("恭喜你，你猜对了！！！")
        print("你一共猜了 %d 次 " % guesstime)
        break
    if counter > 2:
        print("你的次数不足，请充值, Y/N")
        charge = input()
        chargetime = 0
        if charge == "Y":
            print("充值已到账，可继续")
            counter = 1
            chargetime += 1
        else:
            print("你选择放弃")
            break
