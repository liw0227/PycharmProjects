from pyquery import PyQuery
from pprint import pprint
import requests
import time


class Spider:
    @staticmethod
    def decode_html(html_text):
        # print(html_text)
        doc = PyQuery(html_text)
        # print(doc)
        for item in doc.items('.board-wrapper dd'):
            # print(item)
            yield {
                'name': item.find('.name').text(),
                'actors': item.find('.star').text(),
                'time': item.find('.releasetime').text(),
                'score': item.find('.score').text(),
            }

    @staticmethod
    def download_html(url):
        try:
            r = requests.get(url)
            if r.status_code == 200:
                return r.text
            else:
                print('request failed, status is {}'.format(r.status_code))
                return None
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def parse_url(offset):
        url = 'https://maoyan.com/board/4?offset={}'.format(offset)
        html_text = Spider.download_html(url)
        fetched_movies = Spider.decode_html(html_text)
        return fetched_movies