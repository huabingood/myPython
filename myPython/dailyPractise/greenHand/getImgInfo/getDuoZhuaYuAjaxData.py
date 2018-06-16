# -*- encoding:utf8 -*-

import urllib.request


url='https://www.duozhuayu.com/api/home_books?limit=15&after_id=1459008577314'
# header={
#     'Host': 'www.duozhuayu.com',
#     'Connection': 'keep-alive',
#     'x-request-page': '/',
#     'DNT': '1',
#     'x-request-id': '0-1529055184123-97125',
#     'x-api-version': '0.0.1',
#     'x-security-key': '20304898',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
#     'x-timestamp': '1529055184124',
#     'x-request-misc': '{"platform":"browser"}',
#     #'x-request-token': '6461357622c6a7ebcf2210628b4af09ea02da79d52508a73',
#     'x-refer-request-id': '0-1529055183984-37918',
#     'x-user-id': '0',
#     'Accept': '*/*',
#     'Referer': 'https://www.duozhuayu.com/',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Cookie': '_ga=GA1.2.745668255.1527325106; _gid=GA1.2.857278699.1528942302; _gat=1'
# }

header={
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': '_ga=GA1.2.745668255.1527325106; _gid=GA1.2.857278699.1528942302',
    'DNT': '1',
    'Host': 'www.duozhuayu.com',
    'Referer': 'https://www.duozhuayu.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    'x-api-version': '0.0.1',
    'x-refer-request-id': '0-1529058142729-89824',
    'x-request-id': '0-1529058142735-85054',
    'x-request-misc': '{"platform":"browser"}',
    'x-request-page': '/',
    'x-request-prev-page': '/books/48798320138653053',
    'x-request-token': '6461357622c6aab451b78e4a4a55baeb969264fd05861608',
    'x-security-key': '93237155',
    'x-timestamp': '1529058142776',
    'x-user-id': '0'
}



request = urllib.request.Request(url,headers=header)

response = urllib.request.urlopen(request)

print(response.read().decode('utf-8'))