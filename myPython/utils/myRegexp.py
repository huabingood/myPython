# -*- encoding:utf8 -*-

import re

class MyRegexp():
    # 实际上 __init__ 就是构造函数
    def __init__(self,str):
        self.str = str

    # 按照正则表达式取出阅读的人数
    # 传入字符串的例子：posted @ 2018-05-23 16:57 七夜的故事 阅读(149) 评论(0)
    def getReadNum(self):
        subStr = str.split(' ')
        regexp = '(\(\d*\))'
        reResult = re.match(regexp,subStr)
        if reResult:
            print(reResult(1))

    # 在本文件内测试有效
    if __name__ == "__main__":
        MyRegexp('posted @ 2018-05-23 16:57 七夜的故事 阅读(149) 评论(0)').getReadNum()