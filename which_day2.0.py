"""
作者 zyayu
version 2.0
功能：输入某年某月某日，判断这是一年的第几天
字典的运用
"""

from datetime import datetime


def is_leap_year(year):

    """
    判断是否是闰年，结果返回布尔值 真或者假
    """
    is_leap = False
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        is_leap = True
    return is_leap


def main():
    """"
    主函数
    """

    input_data_str = input('请输入时期（yyyy/mm/dd:）')
    input_data = datetime.strptime(input_data_str, '%Y/%m/%d')
    print(input_data)
    year = input_data.year
    month = input_data.month
    day = input_data.day
    # days_in_month_tup = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # 元祖 不能改变
    # days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # list
    # month_days_dict = {1: 31,
    #                    2: 28,
    #                    3: 31,
    #                    4: 30,
    #                    5: 31,
    #                    6: 30,
    #                    7: 31,
    #                    8: 31,
    #                    9: 30,
    #                    10: 31,
    #                    11: 30,
    #                    12: 31}
    day_month_dict = {30: {4, 6, 9, 11},
                      31: {1, 3, 5, 7, 8, 10, 12}}
    days = 0
    for i in range(1, month):
        if i in day_month_dict[30]:       # 是否属于 30 天的月份
            days += 30
        elif i in day_month_dict[31]:
            days += 31
        else:
            days += 28

    if is_leap_year(year):
        days += 1
    print('这是{}年的第{}天'.format(year, days))


if __name__ == '__main__':
    main()