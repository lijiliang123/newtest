# 以下程序用于获取网站网页的标题
import requests
from requests.exceptions import RequestException
import re
import pickle


def save_web_site(url, filename):

    #只在有可能出错的地方才抛出异常,网页内容获取
    try:
        resp = requests.get(url)

    except RequestException as e:
        print(r'geturl failed: unable to get page content:{e}')
        return False

    obj = re.search(r'<title>(.*)</title>', resp.text)  #re，正则表达式匹配字符串

    if not obj:
        print('save failed:title tag not found in the content')
        return False

    title = obj.group(1)  # 获取匹配到的所有结果，不管有没有分组将匹配到的全部拿出来，有参取匹配到的第几个如1

    #只在有可能出错的地方才抛出异常
    #文件写入与读取
    try:
        with open(filename, 'wb') as f:
            pickle.dump(title, f)
        #   f.write(title)
            print(f'save is ok')
        #   return True

        #文件读出
        with open(filename, 'rb') as f:
            line = pickle.load(f)
        #   line=f.read()
            print(line)
            print(f'out put is ok')

    except IOError:
        print(f'save failed: unable to save file.')
        return False
    else:
        return True


def main():
    myurl = input('Pls input your url: ')
    myfile = input('Pls input your filename: ')
    save_web_site(myurl, myfile)
    #save_web_site('https://www.qq.com','qq_title.txt')


if __name__ == '__main__':
    main()


