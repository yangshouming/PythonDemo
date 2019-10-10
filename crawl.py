'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-08-28 14:50:37
@LastEditTime: 2019-08-28 16:22:54
@LastEditors: Please set LastEditors
'''
from urllib import request

with request.urlopen('https://book.douban.com/subject_search?search_text=linux&cat=1001') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))
