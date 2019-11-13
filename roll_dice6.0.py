"""
version 3.0
功能：掷骰子 1.0 随机数 函数 模拟两个骰子 数据可视化 散点图 scatter  科学计算 Numpy 库
import random
 random()  0-1    uniform(a,b) ab 之间随机浮点  randint(a,b) a b 之间锤击整数 choice（） 随机取一个元素   sample(list,k)
 shuffle(list) 顺序打乱
 zip()  两个list 合成一个 tuple 的 列表 但是tuple 元素不可变化，所以要用zip（） 并且用 dict() 转化成字典
"""

import random
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 图标用中文的 命令 SimHei 是字体名字
plt.rcParams['axes.unicode_minus'] = False


def main():
    total_times = 1000
    # 记录 roll 1 记录 roll 2 记录
    roll_1_arr = np.random.randint(1, 7, total_times)  # 生成1000个 1-7 之间 不包含 7 的整数，切实 1000 x 1 的 矩阵 或为向量
    roll_2_arr = np.random.randint(1, 7, total_times)
    roll_3_arr = np.random.randint(1, 7, total_times)
    roll_result_arr = roll_1_arr + roll_2_arr+roll_3_arr
    hist, bins = np.histogram(roll_result_arr, bins=range(3, 19))
    print(hist)
    print(bins)
    # 数据可视化 分布直方图
    plt.hist(roll_result_arr, bins=range(3, 20), density=1, edgecolor='white', linewidth=1, rwidth=0.8)  # density 归一化
    # 坐标值的现实
    tick_label = ['3点', '4点', '5点', '6点',
                  '7点', '8点', '9点', '10点',
                  '11点', '12点', '13点', '14点', '15点', '16点', '17点', '18点']
    tick_pos = np.arange(3, 19) + 0.5
    plt.xticks(tick_pos, tick_label)
    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')
    plt.show()


if __name__ == '__main__':
    main()
