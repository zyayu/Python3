"""
version 1.0
功能：掷骰子 1.0 随机数 函数
import random
 random()  0-1    uniform(a,b) ab 之间随机浮点  randint(a,b) a b 之间锤击整数 choice（） 随机取一个元素   sample(list,k)
 shuffle(list) 顺序打乱
"""

import random


def roll_dice():
    """
    模拟掷骰子
    """
    roll = random.randint(1, 6)
    return roll


def main():
    total_times = 1000
    result_list = [0] * 6
    for i in range(total_times):
        roll = roll_dice()
        for j in range(1, 7):
            if j == roll:
                result_list[j - 1] += 1
    for i, result in enumerate(result_list):  # enumerate 可同时获取索引号 和值   先 索引号 后值
        print('点数是{}，次数是{}，频率是{}'.format(i + 1, result, result / total_times))


if __name__ == '__main__':
    main()
