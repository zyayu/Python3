"""
zyayu
简单爬虫  spider.       requests 模块  对线属性   status_code   400: failure    200:success
获取所有主要城市监测点 数据并保存到 csv 文件中去。
version 1.0
"""
import requests
from bs4 import BeautifulSoup
import csv


# 爬虫 里面 用于解析 html xml 的工具包 找节点.


def get_city_aqi_station(url_path):
    """
    获取URL 的 Aqi的监测点 的数据信息
    """
    r = requests.get(url_path, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    td_list = soup.find_all('td')
    td_list_data = []
    station_data = []
    for td in td_list:
        td_list_data.append(td.text)
    for i in range(int(len(td_list_data) / 6) - 1):
        station_data.append(td_list_data[i * 6:(i + 1) * 6])
    return station_data


def get_city_aqi_header(url_path):
    """
    获取URL 的 AQI 的 表格表头
    """
    r = requests.get(url_path, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    th_list = soup.find_all('th')
    header_name = []
    for i in range(6):
        header_name.append(th_list[i].text)
    return header_name


def get_city_list():
    url_path = 'http://www.air-level.com'
    city_list = []
    r = requests.get(url_path, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    div_list = soup.find('div', {'class': 'citynames'})
    city_link_list = div_list.find_all('a')
    for city_link in city_link_list:
        city_name_chinese = city_link.text
        city_name = city_link['href'][5:]
        city_list.append((city_name_chinese, city_name))
    print(div_list)
    print(city_list)
    return city_list


def main():
    """
    主函数
    """
    city_list = []
    station_data = []
    city_list = get_city_list()
    # 获取表头
    header_name = get_city_aqi_header('http://www.air-level.com/air/beijing/')
    for city in city_list:
        city_name = city[1]
        url_path = 'http://www.air-level.com/air/' + city_name
        # 获取城市 各个监测站的值
        station_data.append(get_city_aqi_station(url_path))
    print(station_data)
    # 把表头 和监测站的值写入CSV 文件中保存
    lines = []
    # 遍历 list 嵌套 list 里面的list元素 可以参考 list [0][0]
    for i in range(len(station_data)):
        for data in station_data[i]:
            lines.append(data)
    f = open("China major cities_aqi_data.csv", 'w', encoding='utf-8', newline='')
    writer = csv.writer(f)
    writer.writerow(header_name)
    for line in lines:
        writer.writerow(line)
    f.close()


if __name__ == '__main__':
    main()
