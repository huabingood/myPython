#-*- coding:utf8 -*-

import urllib.request
import random
from urllib import parse



header={
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
}


request = urllib.request.Request('http://cdn-img.pandabox.top/test.jpg?imageAve',headers=header)

response=urllib.request.urlopen(request)

print(response.read())