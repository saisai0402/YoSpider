import requests
from bs4 import BeautifulSoup as bs

base_url = 'http://www.bytravel.cn/view/index110.html'
l_url = 'http://www.bytravel.cn/view/index110_list.html'
al_url = "http://www.bytravel.cn/view/index110_list{}.html"


def list_url(url):
    li_url = []
    req = requests.get(url)
    html = req.text
    soup = bs(html, 'lxml')
    for a in soup.select('#tctitle > a'):
        list = 'http://www.bytravel.cn/view/' + a.attrs['href']
        li_url.append(list)
    return li_url


def all_url(url1, url2, url3):
    all_url = []
    all_url.extend(list_url(url1))
    all_url.extend(list_url(url2))
    for i in range(1, 2):
        url_list = url3.format(i)
        all_url.extend(list_url(url_list))
    print(all_url)
    return all_url


all_url(base_url, l_url, al_url)
