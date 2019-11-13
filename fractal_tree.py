"""
作者：zyayu
功能 :绘制分形树
主要函数 turtle
日期 19.10.28
version 1.0

"""
# 导入turtle 库

import turtle

# 定义函数 画分形树
"""
绘制分形树函数
"""


def pencolor(branch_length):
    # 判断 branch_length 大小 决定铅笔的颜色
    # 判断 branch_length 有多少个树枝递减的余数 %
    if branch_length % 15 == 0:
        branch_end = 15
    else:
        branch_end = branch_length % 15
    if branch_length == branch_end or branch_length == branch_end + 15:
        turtle.pencolor('green')
    else:
        turtle.pencolor('brown')


def draw_branch(branch_length):

    if branch_length > 5:
        # 判断 branch_length 大小 决定铅笔的颜色
        # 绘制左半边树枝
        pencolor(branch_length)
        turtle.forward(branch_length)
        print('向前，{} px'.format(branch_length))
        turtle.right(20)
        print('右转，{} °'.format(20))
        draw_branch(branch_length-15)
        # 绘制左侧树枝
        turtle.left(40)
        print('左转，{} °'.format(40))
        pencolor(branch_length-15)
        draw_branch(branch_length-15)
        # 返回之前的树枝
        turtle.right(20)
        print('右转，{} °'.format(20))
        pencolor(branch_length)
        turtle.backward(branch_length)

def main():
    turtle.left(90)
    turtle.penup()
    turtle.backward(250)
    turtle.pendown()
    turtle.pensize(5)
    turtle.speed(5)
    n = (input('请输入树枝的开始长度(大于100)： '))
    branch = eval(n)
    # 判断 branch_length 有多少个树枝递减的余数
    draw_branch(branch)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
