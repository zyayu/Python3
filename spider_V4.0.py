"""
zyayu
简单爬虫  spider.       requests 模块  对线属性   status_code   400: failure    200:success
获取图片 爬虫
os 模块
version 1.0
"""
import requests
from bs4 import BeautifulSoup
import os


# 爬虫 里面 用于解析 html xml 的工具包 找节点.


def get_img_data(url_path):
    """
    获取图片专辑中每一张大图的url
    """
    r = requests.get(url_path, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    a_data = soup.find('div', {'class': "il_img"})
    dir_name = a_data.find('a')['title']
    img_album_url = 'https://www.ivsky.com' + a_data.find('a')['href']  # 获取 图片系列专辑的url 下一步爬 这一个url
    r_1 = requests.get(img_album_url, timeout=30)
    soup_1 = BeautifulSoup(r_1.text, 'lxml')
    img_album_list = soup_1.find_all('div', {'class': "il_img"})  # 可遍历的 div  每一个div 里只有一个 <a..
    img_data_list = []
    for img_album in img_album_list:
        img_data_list.append(img_album.find('a')['href'])
    img_data = []
    for list in img_data_list:
        img_data.append('https://www.ivsky.com' + list)
    # print(img_album_list)   调试的时候用
    # print(img_data_list)
    print(img_data)
    # print(dir_name)
    return [img_data, dir_name]


def get_img_url(img_data):
    r = requests.get(img_data, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    div_list = soup.find('div', {'id': "pic_con"})
    img_url = div_list.img['src']
    print(div_list)
    print(img_url)
    return img_url


def main():
    """
    主函数
    """
    url_path = 'https://www.ivsky.com/bizhi/huihua/'
    img_data, dir_name = get_img_data(url_path)
    # 下载图片
    save_path = 'C:/Users/think/Pictures/' + dir_name
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    i = 0
    for data in img_data:
        img_url = 'http:'+get_img_url(data)
        img_pic = requests.get(img_url)
        with open(save_path + '/' + str(i) + '.jpg', 'wb') as fp:  # 文件名到相应文件夹
            fp.write(img_pic.content)
        i += 1


if __name__ == '__main__':
    main()
