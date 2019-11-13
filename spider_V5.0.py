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


def get_dir_name(url_path):
    """
    获取图集名称和图集的url
    """
    r = requests.get(url_path, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    div_list = soup.find_all('div', {'class': "il_img"})
    print(div_list)
    dir_name = []
    img_album_url = []
    for div in div_list:
        dir_name.append(div.find('a')['title'])
        img_album_url.append('https://www.ivsky.com' + div.find('a')['href'])
    return [img_album_url, dir_name]


def get_img_web_url(img_album_url):
    r = requests.get(img_album_url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    img_album_url_list = soup.find_all('div', {'class': "il_img"})  # 可遍历的 div  每一个div 里只有一个 <a..
    img_web_url_list = []
    for img_album_url in img_album_url_list:
        img_web_url_list.append(img_album_url.find('a')['href'])
    img_web_url = []
    for list in img_web_url_list:
        img_web_url.append('https://www.ivsky.com' + list)
    return img_web_url


def get_img_url(img_web_url):
    r = requests.get(img_web_url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    div_list = soup.find('div', {'id': "pic_con"})
    img_url = div_list.img['src']
    return img_url


def main():
    """
    主函数
    """
    url_path = 'https://www.ivsky.com/bizhi/huihua/'
    # 获取系列名称 ---文件夹名称，并建立文件夹.
    img_album_url_list, dir_name_list = get_dir_name(url_path)
    dir_name_ = []
    save_path = []
    for dir_name in dir_name_list:
        dir_name_.append(dir_name)
        save_path.append('C:/Users/think/Pictures/' + dir_name)
        for i in range(len(save_path)):
            if not os.path.exists(save_path[i]):
                os.makedirs(save_path[i])
        # 文件夹建立好了并且得到了系列图集的url album_ url
        # 开始获取图集里面每一张图片的页面url
    j = 0  # 记录 这是
    #  开始分图集下载图片 遍历 img_album_url_list 中 这是一个list【list】
    for img_album_url in img_album_url_list:
        img_web_url = get_img_web_url(img_album_url)
        print(img_web_url)
        # 获得每一张图的页面url 之后 获取 大图的url
    # 下载文件并储存,并给出提示 正在下载哪一个图集
        print('{}图集正在下载...'.format(dir_name_[j]))
        i = 0
        for img_web in img_web_url:
            img_url = 'http:' + get_img_url(img_web)
            img_pic = requests.get(img_url)
            with open(save_path[j] + '/' + str(i) + '.jpg', 'wb') as fp:  # 文件名到相应文件夹
                fp.write(img_pic.content)
            i += 1
        print('done')
        j += 1  # save_path 换下一个 文件夹
    print('所有图集下载完毕')


if __name__ == '__main__':
    main()
