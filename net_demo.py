# /usr/local/bin/python3
# --*-- coding:utf-8 --*--
# __Author__ = 'Jieer'

import urllib.request as ur

# url = 'http://www.iheartquotes.com/api/v1/random'
url ='http://www.baidu.com'
conn = ur.urlopen(url)

print(conn)

data = conn.read()

print(data)

print(conn.status,conn.getheader('Content-Type'))

head_list = [(head,value) for head,value in conn.getheaders()]

print(head_list)

import requests

url = 'http://www.baidu.com'

resp = requests.get(url)

print(resp.status_code)


# from bottle import route,run,static_file
#
# # @route('/')
# # def home():
# #     return "'It isn't fancy,but it's my home page"
#
# @route('/')
# def main():
#     return static_file('index.html',root='.')
#
# @route('/echo/<thing>')
# def echo(thing):
#     return "Say hello to my little friend: %s!"% thing
#
# run(host='localhost',port=9999)

# from flask import Flask, render_template
#
# # app = Flask(__name__,static_folder='.',static_url_path='')
# app = Flask(__name__)
# @app.route('/')
# def home():
#     return app.send_static_file('index.html')
#
# @app.route('/echo/<thing>/<place>')
# def echo(thing,place):
#     # return "Say hello to my little friend:%s"%thing
#     return render_template('flask2.html',thing = thing,place = place)
#
# app.run(port=9999,debug=True)

# import webbrowser
#
# url = 'http://www.python.org/'
#
# webbrowser.open(url)

#
# def get_links(url):
#     import requests
#     from bs4 import BeautifulSoup as soup
#     result = requests.get(url)
#     page = result.text
#     doc = soup(page)
#     links = [element.get('href') for element in doc.find_all('a')]
#     return links
#
# # if __name__ == '__main__':
#
#     import sys
#
#     # for url in sys.argv[1:]:
#     #     print('links in',url)
# for num,link in enumerate(get_links('http://www.python.org'),start=1):
#     print(num,link)
# print()

for num,i in enumerate(list('lijieer')):

    print(num,"--->",i)



