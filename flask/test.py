import datetime

# def type_checker(function):
#     def inner_func(digit, digit2):
#         if (type(digit) != int) or (type(digit2) != int):
#             print('Wrong Type')
#             return
#         return function(digit, digit2)
#     return inner_func
#
# @type_checker
# def divide(digit, digit2):
#     return digit * digit2
#
# print(divide(3, 'd'))

# def decorator1(function):
#     def wrapper():
#         print('decorator1')
#         function()
#
#     return wrapper
#
#
# def decorator2(function):
#     def wrapper():
#         print('decorator2')
#         function()
#
#     return wrapper
#
# @decorator1
# @decorator2
# def hello():
#     print('hello')
#
# hello()

def mark_bold(function):
    def wrapper(*args, **kwargs):
        return '<b>' + function(*args, **kwargs) + '</b>'
    return wrapper


print('{} {}'.format(10, 100))
print('{0} {2} {1} {0}'.format(10, 100, 300))

print('{aa} {bb}'.format(aa='aadddd', bb='bbccc'))

def html_creator(tag):
    def text_wrapper(msg):
        return '<{0}>{1}</{0}>'.format(tag, msg)
    return text_wrapper

h1_html = html_creator('h1')

def datetime_decorator(func):           # <--- datetime_decorator 는 데코레이터 이름, func 가 이 함수 안에 넣을 함수가 됨
    def wrapper():                      # <--- 호출할 함수를 감싸는 함수
        print ('time ' + str(datetime.datetime.now())) # <--- 함수 앞에서 실행할 내용
        func()                          # <--- 함수
        print (datetime.datetime.now()) # <--- 함수 뒤에서 실행할 내용
    return wrapper                      # <--- closure 함수로 만든다.


@datetime_decorator    # @데코레이터
def logger_login_david():
     print ("David login")

logger_login_david()


import requests
from bs4 import BeautifulSoup
import datetime

res = requests.get('https://davelee-fun.github.io/blog/crawl_html_css.html')
soup = BeautifulSoup(res.content, 'html.parser')
# a 태그이면서 href 속성 값이 특정한 값을 갖는 경우 탐색
link_titles = soup.select("ul#hobby_course_list > li")
data = list()

for link_title in link_titles:
    data.append(link_title.get_text())
