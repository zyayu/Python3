""""
 分支结构
"""
"""
用户身份验证

Version: 0.1
Author: zyayu
"""

username = input('请输入用户名: ')
password = input('请输入口令: ')
# 用户名是admin且密码是123456则身份验证成功否则身份验证失败
if username == 'admin' and password == '123456':
    print('身份验证成功!')
else:
    print('身份验证失败!')
"""
分段函数求值
		3x - 5	(x > 1)
f(x) =	x + 2	(-1 <= x <= 1)
		5x + 3	(x < -1)

Version: 0.1
Author: zyayu
"""
x = float(input("请输入x 值： "))
if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:  # 实际上后面的 and 多余。
        y = x + 2
    else:
        y = 5 * x + 3
print("f(%.2f) = %.2f" % (x, y))
"""
练习 1 英制单位和公制单位厘米转换
Version： 0.1
Author： zyayu
"""
Value = float(input("请输入长度: "))
unit = input("请输入单位: ")
if unit == "inc" or unit == "英寸":
   print("%.2f英寸 = %.2f厘米" % (Value, Value * 2.54))
elif unit == "cm" or unit == "厘米":
    print("%.2f厘米 = %.2f英寸" % (Value, Value / 2.54))
else:
    print("请输入有效的单位，谢谢合作")
