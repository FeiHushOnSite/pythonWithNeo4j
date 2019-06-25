# coding:utf-8
#
# 把qq.ip138.com/train/上面的列车时刻表抓取解析出来，输出在命令行显示，并存入一个文件train_time.text
#
import requests
import time
from bs4 import BeautifulSoup
import random

BSLIB = 'html5lib'
BASE_URL = 'http://qq.ip138.com'
UA = ["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
      "Mozilla/5.0 (X11; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0",
      "Mozilla/5.0 (X11; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0",
      "Mozilla/5.0 (X11; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0",
      "Mozilla/5.0 (X11; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0"]


def get_province(province, url, file):
    print(province)
    file.write("%s\n" % province)
    HEADERS = {'user-agent': random.choice(UA)}
    r = requests.get(url, headers=HEADERS)
    s = BeautifulSoup(r.text.encode(r.encoding).decode('gbk'), BSLIB)
    C = s.select('div > table > tbody > tr > td > a')
    for c in C:  # 每个城市
        get_city(c.text, BASE_URL + c.get('href'), file)
    time.sleep(random.random() * 30)  # 防止因访问频繁而被拒绝请求


def get_city(city, url, file):
    print('  %s' % city)
    file.write("  %s\n" % city)
    HEADERS = {'user-agent': random.choice(UA)}
    r = requests.get(url, headers=HEADERS)
    s = BeautifulSoup(r.text.encode(r.encoding).decode('gbk'), BSLIB)
    T = s.select('div#checilist > table > tbody > tr')
    for t in T:  # 每个车次
        t_text = "\t"
        tt = t.select('td')
        for i in tt:  # 每个车次的具体每个信息用\t隔开
            t_text += "%s\t" % i.text
        print(t_text)
        file.write('%s\n' % t_text)
    time.sleep(random.random() * 4)  # 防止因访问频繁而被拒绝请求


if __name__ == '__main__':
    out_file = open('train_time.txt', 'w')
    url = BASE_URL + '/train/'
    HEADERS = {'user-agent': random.choice(UA)}
    r = requests.get(url, headers=HEADERS)
    s = BeautifulSoup(r.text.encode(r.encoding).decode('gbk'), BSLIB)
    P = s.select('table[width="600"] > tbody > tr > td > a')
    for p in P:  # 每个省份
        get_province(p.text, BASE_URL + p.get('href'), out_file)
