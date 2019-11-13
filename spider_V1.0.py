"""
zyayu
简单爬虫  spider.       requests 模块  对线属性   status_code   400: failure    200:success
获取城市监测点 数据并保存到 csv 文件中去。
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
    for i in range(int(len(td_list_data)/6)-1):
        station_data.append(td_list_data[i*6:(i+1)*6])
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


def main():
    """
    主函数
    """
    city_name = input('请输入城市的名字（拼音）：')
    url_path = 'http://www.air-level.com/air/' + city_name + '/'
    # 获取表头
    header_name = get_city_aqi_header(url_path)
    # 获取城市 各个监测站的值
    station_data = get_city_aqi_station(url_path)
    # 把表头 和监测站的值写入CSV 文件中保存
    f = open(city_name+"_aqi_data.csv", 'w', encoding='utf-8', newline='')
    writer = csv.writer(f)
    writer.writerow(header_name)
    for data in station_data:
        writer.writerow(data)
    f.close()


if __name__ == '__main__':
    main()
