"""
zyayu
简单爬虫  spider.       requests 模块  对线属性   status_code   400: failure    200:success
获取图片 爬虫
version 1.0
"""
import requests
from bs4 import BeautifulSoup
import csv


# 爬虫 里面 用于解析 html xml 的工具包 找节点.


def get_img_data(url_path):
    """
    获取URL的图片信息
    """
    r = requests.get(url_path, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    a_data = soup.find('div', {'class': "col-md-4 rightbar text-center"})
    img_data = a_data.find('a').img['src']   # 获取a 的内容是 img 里面的 src 属性。
    print(img_data)
    return img_data


def main():
    """
    主函数
    """
    url_path = 'http://www.air-level.com/air/shanghai/'
    img_data = get_img_data(url_path)
    img = requests.get(img_data)
    fp = open('123.jpg', 'wb')  # 文件名
    fp.write(img.content)
    fp.close()


if __name__ == '__main__':
    main()
