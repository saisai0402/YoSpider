from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from YoSpider.items import YospiderItem
from bs4 import BeautifulSoup as bs
import requests

id = '110'

base_url = 'http://www.bytravel.cn/view/index{}.html'.format(id)
l_url = 'http://www.bytravel.cn/view/index{}_list.html'.format(id)
al_url = 'http://www.bytravel.cn/view/index{}'.format(id) + '_list{}.html'


def list_url(url):
    li_url = []
    req = requests.get(url)
    html = req.text
    soup = bs(html, 'lxml')
    for a in soup.select('#tctitle > a'):
        list = 'http://www.bytravel.cn' + a.attrs['href']
        li_url.append(list)
    return li_url


def all_url(url1, url2, url3):
    all_url = []
    all_url.extend(list_url(url1))
    all_url.extend(list_url(url2))
    for i in range(1, 20):
        url_list = url3.format(i)
        all_url.extend(list_url(url_list))
    print(all_url)
    return all_url


class qulishi(CrawlSpider):
    name = 'YoSpider'
    start_urls = ['http://www.bytravel.cn/Landscape/2/panshan.html']

    def parse(self, response):
        item = YospiderItem()
        selector = Selector(response)
        html = response.text
        soup = bs(html, 'lxml')
        title = ''.join(selector.xpath('//*[@id="page_left"]/div[2]/h1/text()')[0].extract())
        article = []
        if len(soup.select('#page_left > div.f14 > div.f14b')) > 0:
            for p in soup.select('#page_left > div.f14 > div.f14b'):
                article.append(p.text.strip())
        article.append(selector.xpath('//*[@id="page_left"]/div[7]/text()')[0].extract())
        if len(soup.select('#page_left > div.f14 > p')) > 0:
            for p in soup.select('#page_left > div.f14 > p'):
                article.append(p.text.strip())
        prefecture_1 = ''.join(selector.xpath('//*[@id="page_left"]/div[1]/div/a[2]/text()')[0].extract())
        prefecture_2 = ''.join(selector.xpath('//*[@id="page_left"]/div[1]/div/a[3]/text()')[0].extract())
        try:
            prefecture_3 = ''.join(selector.xpath('//*[@id="page_left"]/div[1]/div/a[4]/text()')[0].extract())
        except:
            prefecture_3 = ''

        content = '\n'.join(article)
        post_status = ''.join('draft')
        item['post_title'] = title
        item['post_keywords'] = title
        item['post_content'] = content
        item['post_status'] = post_status
        item['post_prefecture_1'] = prefecture_1
        item['post_prefecture_2'] = prefecture_2
        item['post_prefecture_3'] = prefecture_3
        yield item
        urls = all_url(base_url, l_url, al_url)

        for url in urls:
            yield Request(url, callback=self.parse)
