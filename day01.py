"""
赋值运算符和复合复制运算
version 0.1
Author： zyayu
"""
a = 10
b = 3
a += b  # 相当于：a = a + b  a=13
a *= a + 2  # 相当于：a = a * (a + 2)   a=13*15
print(a)
"""
比较、逻辑和算身份运算符的使用

Version: 0.1
Author: zyayu
"""
flag0 =1 ==1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print('flag0 =', flag0)  # flag0 = True
print('flag1 =', flag1)  # flag1 = True
print('flag2 =', flag2)  # flag2 = False
print('flag3 =', flag3)  # flag3 = False
print('flag4 =', flag4)  # flag4 = True
print('flag5 =', flag5)  # flag5 = False
print(flag1 is True)  # True
print(flag2 is not False)  # False

"""
将华氏温度转换为摄氏温度

Version: 0.1
Author: zyayu
"""

f = float(input('请输入华氏温度: '))  # C语言里面的 snf
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
"""
输入圆的半径计算周长和面积

Version: 0.1
Author: zyayu
"""
import math
radius = float(input("请输入圆的半径："))
perimeter = 2 * math.pi * radius
area = math.pi * math.pow(radius, 2)  # pow(x,y) x的Y 次方
print("周长： %.2f" % perimeter)
print("面积： %.2f" % area)
"""
输入年份 如果是闰年输出True 否则输出False

Version: 0.1
Author: zyayu
"""
year = int(input("请输入年份： "))  # 获取屏幕输入的数字
#  如果代码太长携程遗憾不便于阅读，可以使用\代码进行拆行
is_leap =(year % 4 == 0 and year % 100 !=0) or \
         year % 400 == 0
if is_leap:
    outcome = "YES"
else:
    outcome = "No"
print("year is leap ?  Answer is %s " % outcome)  # %d int %f %s  print 格式化输出。



