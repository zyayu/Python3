"""
作者 zyayu
功能： jason csv 文件 读取 操作  lambada 函数
version 1.0
"""
import json


def process_json_file(file_path):
    """
    文件 打开 操作  关闭

    """
    f = open(file_path, mode='r', encoding='UTF-8')
    city_list = json.load(f)
    return city_list


def main():
    """
    主函数
    """
    file_path = input('请输入文件名称： ')
    city_list = process_json_file(file_path)
    city_list.sort(key=lambda city: city['aqi'])
    top5 = city_list[:5]
    f = open('top5_aqi.json', mode='r', encoding='UTF-8')
    json.dump(top5, f, ensure_ascii=False)
    f.close()
    print(city_list)


if __name__ == '__main__':
    main()
