"""
作者:zyayu
version 1.0
功能：判断密码强度
"""


def check_num_exist(password_str):
    for c in password_str:
        if c.isnumeric():
            return True
    return False


def check_letter_exist(password_str):
    for c in password_str:
        if c.isalpha():
            return True
    return False


def main():
    # 密码强度
    strength_level = 0
    # 获取用户的密码
    password_str = input('请设置你的密码:')
    # 规则1 密码长度要大于8位
    if len(password_str) < 8:
        print('密码至少需要8位')
    else:
        strength_level += 2
    # 规则2 判断密码是否含有数字
    if check_num_exist(password_str):
        strength_level += 2
    # 规则3 判断密码是否含有字母
    if check_letter_exist(password_str):
        strength_level += 2
    print('您设置的密码强度是：', strength_level)
    for i in range(strength_level):
        print('*', end="\t")


if __name__ == '__main__':
    main()
