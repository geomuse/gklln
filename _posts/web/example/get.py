url = 'https://www.qimao.com/shuku/2081352-17612244040003/'
import requests 

respone = requests.get(url)
print(respone.status_code)
print(respone.text)