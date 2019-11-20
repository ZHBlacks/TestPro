'''
Created on 2019年11月12日

@author: Veryci
'''
import requests

test_url = "https://www.jianshu.com"
# from_data = {
#         "_method":"delete",
#         "authenticity_token":"9ozgwsnXBNXleBKNw8CMJk4vR0E7wZerj592hKNZvaI0zypwIEiPdOOegEcVmJopD7Gt48gyKoOR1zE77SZ2mg=="
#     }

login_out = requests.get(test_url)
print(login_out.status_code)
print(login_out.text)


