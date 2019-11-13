"""
  循环结构 输出乘法口诀表(九九表)

Version: 0.1
Author: 骆昊
"""

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()  # 输出空 则为空一行。 很妙！！
"""
输入一个正整数判断它是不是素数

Version: 0.1
Author: zyayu
"""
from math import sqrt
num = int(input("请输入一个正整数:"))
is_prime = True
for i in range(2, num, 1): # 实际迭代到 num的平方根之前还没有整除的那么后面，后面也不会有了。
    if num % i == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print("%d 是一个素数" % num)
else:
    print("%d 不是一个素数" % num)
"""
输入两个正整数计算它们的最大公约数和最小公倍数
巧用递减循环求最大公约数
最大公倍数 则是两个数的乘积除以公约数。
Version: 0.1
Author: zyayu
"""
x = int(input("请给第一个数: "))
y = int(input("请给第二个数: "))
if x > y:
    x, y = y, x  # 相当于 a = x x = y y = a , 既是xy 数值互换。
# 从 x y 中 最小的数开始递减循环 缩减迭代次数
for factor in range(x, 0, -1):
    if y % factor == 0 and x % factor == 0:
        print("%d 和 %d 的最大公约数是 %d" % (x, y, factor))
        print("%d 和 %d 的最大公倍数是 %d" % (x, y, x * y // factor))
        break  # 缩进控制 属于哪一个循环 或者分支里面， 缩进在python 里面，非常重要，空格键不能随意加。

