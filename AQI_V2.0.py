"""
作者 zyayu
功能： jason csv 文件 读取 操作  lambada 函数
version 1.0
"""
import json
import csv
import pandas as pd


def process_csv_file(file_path):
    """
    文件 打开 操作  关闭

    """
    f = open(file_path, mode='r', encoding='UTF-8', newline='')
    reader = csv.reader(f)  # 得到可遍历的数据
    # df = pd.DataFrame(reader)   # python 区分 大小写 数据结构 类型 可以直接转换
    # head = df.head(5)
    # print(head)
    data_list = []
    for row in reader:
        data_list.append(row)
    f.close()
    return data_list


def main():
    """
    主函数
    """
    file_path = input('请输入文件名称： ')
    data_list = process_csv_file(file_path)
    f = open('pima-indians-diabetes.data.json', mode='w', encoding='UTF-8')
    json.dump(data_list, f, ensure_ascii=False)
    f.close()
    print(data_list)


if __name__ == '__main__':
    main()
