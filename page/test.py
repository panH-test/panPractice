import io
import os
import sys
import requests
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')  # 编码格式


def urlBS(url):  # 定义发起请求函数
    resp = requests.get(url)
    html = resp.content.decode(encoding='UTF-8')
    soup = BeautifulSoup(html,'lxml')  # 解析网页
    # print(soup)
    return soup


# firsturl = 'http://www.rensheng5.com/zx/onduzhe/'  # 目标地址
# urlBS(firsturl)


def mmmm(url):
    soup = urlBS(url)  # 调用函数
    lis = soup.find('body') # 从网页获取的信息
    alink = lis.find('div',class_='page').find('a')['href']
    print(alink)

    # 数据保存的目录(os.getced()创建文件夹)
    path = os.getcwd() + u'/爬取的文章/'
    if not os.path.isdir(path):  # 判断是否有这个文件夹
        os.mkdir(path)
    for i in lis:
        try:
            nurl = i.find('a')['href']
            print(nurl)
        except:
            print('shibai')
        # 请求每篇文章
        result = urlBS(nurl)  # 调用函数
        title = result.find('div', class_="news_detail").find('h1').get_text()  # 获取标题
        print(title)
        # writer = result.find('div', class_="artinfo").get_text()  # 获取作者
        # print(writer)
        # 保存的文件格式:
        filename = path + title + '.txt'
        print(filename)

        # 写入操作
        new = open(filename, 'w')
        new.write('<<' + title + '>>\n\n')  # 写入标题
        # new.write(writer + '\n\n')  # 写入作者
        text = result.find('div', class_="content").find('p').get_text()
        new.write(text)  # 写入内容
        new.close()  # 关闭


if __name__ == '__main__':

    mmmm('http://www.vanturn.cn/news/525.html')
