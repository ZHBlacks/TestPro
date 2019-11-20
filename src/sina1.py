'''
Created on 2019年11月6日

@author: Veryci
'''
import requests
test_url = "http://www.sina.com.cn"
response = requests.get(test_url)
print(response.status_code)
print(response.headers)
# print(response.text)