"""
百分制成绩转换为等级制成绩

Version: 0.1
Author: zyayu
"""
score = float(input("please input your score: "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "E"
print("YOUR SCORE IS (%.1f) AND THE GRADE IS (%s) " % (score, grade))
if grade == "E":
    print("PLEASE WORK HARDER TO MAKE A DIFFERENCE")
else:
    print("score Recorded ")
"""
判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积

Version: 0.1
Author: zyayu
"""

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5  # 海伦公式  ** 0.5 代表0.5次方  等同于 POW（）
    print('面积: %f' % area)
else:
    print('不能构成三角形')

