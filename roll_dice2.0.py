"""
version 2.0
功能：掷骰子 1.0 随机数 函数 模拟两个骰子
import random
 random()  0-1    uniform(a,b) ab 之间随机浮点  randint(a,b) a b 之间锤击整数 choice（） 随机取一个元素   sample(list,k)
 shuffle(list) 顺序打乱
 zip()  两个list 合成一个 tuple 的 列表 但是tuple 元素不可变化，所以要用zip（） 并且用 dict() 转化成字典
"""

import random


def roll_dice():
    """
    模拟掷骰子
    """
    roll = random.randint(1, 6)
    return roll


def main():
    total_times = 100
    # 初始化列表 点数列表 和频数列表
    result_list = [0] * 11
    roll_list = list(range(2, 13))
    roll_dict = dict(zip(roll_list, result_list))  # 前面是不变的Key 后面是 值
    for i in range(total_times):
        roll_1 = roll_dice()
        roll_2 = roll_dice()
        roll_result = roll_1 + roll_2
        for j in range(2, 13):
            if j == roll_result:
                roll_dict[j] += 1
    for i, result in roll_dict.items():
     print('点数是{}，次数是{}，频率是{}'.format(i, result, result / total_times))


if __name__ == '__main__':
    main()
