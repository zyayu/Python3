"""
作者 zyayu
version 1.0
52周存钱挑战

"""
"""
主函数
"""
# 全局变量
money_list = []  # 记录每周的存款数列表
saving_list = []  # 记录每周的存款数列表


def main():
    money_per_week = float(input('请输入第一周存入的金额：'))  # 每周要存的钱
    increase_money = float(input('请输入每周递增的金额：'))  # 每周要存递增的钱
    week_no_max = float(input('请输入要存多少周：'))  # 最大的周数
    saving_money(money_per_week, week_no_max, increase_money)
    n = int(input('您想查询第几周要存的款，以及累计余额，请输入数字1-52：'))
    print('您的查询结果是：第{}周，存入{}元，累计余额{}'.format(n, money_list[n - 1], saving_list[n - 1]))


def saving_money(money_per_week, week_no_max, increase_money):
    import math
    week_no = 1  # 周数
    global money_list  # 这样函数内部用的也是 全局变量的那个10
    global saving_list
    while week_no <= week_no_max:  # 缩进非常重要。 如果while 顶格写，会出现 未定义。 因为 定义是在main 函数里面

        # 存钱操作

        money_list.append(money_per_week)  # 在列表的最后增加一个元素,记录每周要存的钱
        saving = math.fsum(money_list)
        saving_list.append(saving)  # 在列表的最后增加一个元素 记录累计余额
        # 输出信息
        print('第{}周，存入{}元，累计余额{}'.format(week_no, money_per_week, saving))
        money_per_week += increase_money
        week_no += 1
    return saving_list, money_list


if __name__ == '__main__':
    main()
