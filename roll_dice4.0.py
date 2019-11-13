"""
version 3.0
功能：掷骰子 1.0 随机数 函数 模拟两个骰子 数据可视化 散点图 scatter
import random
 random()  0-1    uniform(a,b) ab 之间随机浮点  randint(a,b) a b 之间锤击整数 choice（） 随机取一个元素   sample(list,k)
 shuffle(list) 顺序打乱
 zip()  两个list 合成一个 tuple 的 列表 但是tuple 元素不可变化，所以要用zip（） 并且用 dict() 转化成字典
"""

import random
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']   # 图标用中文的 命令 SimHei 是字体名字
plt.rcParams['axes.unicode_minus'] = False


def roll_dice():
    """
    模拟掷骰子
    """
    roll = random.randint(1, 6)
    return roll


def main():
    total_times = 1000
    # 记录 roll 1 记录 roll 2 记录
    roll_list = []
    for i in range(total_times):
        roll_1 = roll_dice()
        roll_2 = roll_dice()
        roll_list.append(roll_1 + roll_2)
    # 数据可视化 分布直方图
    plt.hist(roll_list, bins=range(2, 14), normed=1, edgecolor='white', linewidth=10)  # normed 归一化
    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')
    plt.show()


if __name__ == '__main__':
    main()
