#codeing:utf-8
import requests
# 请求url
url = "http://www.baidu.com"
# 请求参数
payload = {
    "mobilephone":"1530272****",
    "pwd":"123456"
}
# form表单形式，参数用data
res = requests.post(url, data=payload)
print(res.text)
