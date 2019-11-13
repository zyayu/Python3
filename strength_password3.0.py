"""
作者:zyayu
version 1.0
功能：判断密码强度，并保存到文件中 ASCII Unicode UTF-8 常用的编码 多行 用\n 表示换行。
文件的操作   打开文件  操作文件 （读写 等）--关闭文件
open(filename mode)  mode   模式    r  只读 W  文件不存在 报错 只写 文件不存在 自动创建  a  在文件末尾附加   r+  读写

写的操作
 write（）
 writelines（）字符串写入
 close（） 关闭
"""


def check_num_exist(password_str):
    number_exist = False
    for c in password_str:
        if c.isnumeric():
            number_exist = True
            break
    return number_exist


def check_letter_exist(password_str):
    letter_exist = False
    for c in password_str:
        if c.isalpha():
            letter_exist = True
            break
    return letter_exist


def main():
    set_times = 3
    while set_times > 0:

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
        else:
            print('密码至少包含一个数字')
        # 规则3 判断密码是否含有字母
        if check_letter_exist(password_str):
            strength_level += 2
        else:
            print('密码至少包含一个字母')

        # 存入文件操作
        # 密码强度描述转换
        if strength_level == 2:
            strength_describe = '弱'
        elif strength_level == 4:
            strength_describe = '中'
        else:
            strength_describe = '强'

        f = open('password_3.0.txt', 'a')
        f.write('密码：{}， 密码强度等级：{}，密码强度为：{} \n'.format(password_str, strength_level, strength_describe))
        f.close()
        if strength_level == 6:
            print('您设置的密码强度是 {}，恭喜合格了：'.format(strength_level))
            for i in range(strength_level):
                print('*', end="\t")
            break  # 终止 while 循环
        else:
            print('您设置的密码强度是 {}，密码设置不合格，请重新设置：'.format(strength_level))
            set_times -= 1
    if set_times <= 0:
        print('您设置密码设置不合格次数过多，密码设置失败！')


if __name__ == '__main__':
    main()
