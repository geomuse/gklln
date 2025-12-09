url =  "https://engoo.com/app/daily-news/article/shibuya-cancels-new-years-countdown-again/NEz4VNCDEfCROadI_eb26w"

import requests 

respone = requests.get(url)
print(respone.status_code)