"""
作者:zyayu
version 1.0
功能：判断密码强度，并保存到文件中 ASCII Unicode UTF-8 常用的编码 多行 用\n 表示换行。
文件的操作   打开文件  操作文件 （读写 等）--关闭文件
open(filename mode)  mode   模式    r  只读 W  文件不存在 报错 只写 文件不存在 自动创建  a  在文件末尾附加   r+  读写
read()
readlines()
readline()

写的操作
 write（）
 writelines（）字符串写入
 close（） 关闭


类别  Class
文件操作 封装 成类
"""


class PasswordTool:
    """
        密码工具类
    """

    def __init__(self, password):
        self.password = password
        self.strength_level = 0

    def process_password(self):
        # 规则1 密码长度要大于8位
        if len(self.password) < 8:
            print('密码至少需要8位')
        else:
            self.strength_level += 2
        # 规则2 判断密码是否含有数字
        if self.check_num_exist():
            self.strength_level += 2
        else:
            print('密码至少包含一个数字')
        # 规则3 判断密码是否含有字母
        if self.check_letter_exist():
            self.strength_level += 2
        else:
            print('密码至少包含一个字母')

    # 类的方法
    def check_num_exist(self):
        number_exist = False
        for c in self.password:
            if c.isnumeric():
                number_exist = True
                break
        return number_exist

    def check_letter_exist(self):
        letter_exist = False
        for c in self.password:
            if c.isalpha():
                letter_exist = True
                break
        return letter_exist


class FileTool:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_to_file(self, line):
        f = open(self.file_path, 'a')
        f.write(line)
        f.close()

    def read_from_file(self):
        f = open(self.file_path, 'r')
        lines = f.readlines()
        f.close()
        return lines


def main():
    set_times = 3
    # 实例化对线
    file_path = 'password_6.0.txt'
    file_tool = FileTool(file_path)
    while set_times > 0:

        # 密码强度
        strength_level = 0
        # 获取用户的密码
        password_str = input('请设置你的密码:')
        # 实例化类 对象
        password_tool = PasswordTool(password_str)
        # 调用 类的方法
        password_tool.process_password()
        # 存入文件操作
        # 密码强度描述转换
        if password_tool.strength_level == 2:
            strength_describe = '弱'
        elif strength_level == 4:
            password_tool.strength_describe = '中'
        else:
            strength_describe = '强'
        # 确认写入的格式...
        lines = '密码：{}， 密码强度等级：{}，密码强度为：{} \n'.format(password_str, password_tool.strength_level, strength_describe)
        file_tool.write_to_file(lines)
        if password_tool.strength_level == 6:
            print('您设置的密码强度是 {}，恭喜合格了：'.format(password_tool.strength_level))
            for i in range(password_tool.strength_level):
                print('*', end="\t")
            break  # 终止 while 循环
        else:
            print('您设置的密码强度是 {}，密码设置不合格，请重新设置：'.format(password_tool.strength_level))
            set_times -= 1
    if set_times <= 0:
        print('您设置密码设置不合格次数过多，密码设置失败！')

        lines = file_tool.read_from_file()


if __name__ == '__main__':
    main()
