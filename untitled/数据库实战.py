from pyquery import PyQuery
from pprint import pprint
import requests
import time
import pandas as pd



def decode_html(html_text):
    '''解析网页的电影数据'''
    doc = PyQuery(html_text)
    for item in doc.items('.board-wrapper dd'):
        yield {
        'name': item.find('.name').text(),
        'actors': item.find('.star').text(),
        'time': item.find('.releasetime').text(),
        'score': item.find('.score').text()
        }


def download_html(url):
    '''下载的html text'''
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.text
        else:
            print('request failed ,status is {}'.format(r.status_code))
            return None
    except Exception as e:
        print(e)
        return None


def parse_url(offset):
    '''解析网页'''
    url = 'https://maoyan.com/board/4?offset={}'.format(offset)
    html_text = download_html(url)
    for each_movie in decode_html(html_text):
        pprint(each_movie)


def main():
    '''多页面1-10'''
    for offset in range(10, 100, 10):
        parse_url(offset)

main()
s = pd.Series(parse_url())
print(s)