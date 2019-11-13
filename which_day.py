"""
作者 zyayu
version 1.0
功能：输入某年某月某日，判断这是一年的第几天
"""

from datetime import datetime
def is_leapyear(year):
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
    days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leapyear(year):
        days_in_month_list[1] = 29
    days = sum(days_in_month_list[: month-1]) + day
    print('这是{}年的第{}天'.format(year, days))


if __name__== '__main__':
    main()