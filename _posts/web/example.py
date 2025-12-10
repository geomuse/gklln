import requests 
from bs4 import BeautifulSoup

if __name__ == "__main__":

    headers = {
        'User-Agent': 'Mozilla/5.0',
    }
    response = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)', headers=headers)
    soup = BeautifulSoup(response.text,'html.parser')

    content = soup.select('p')

    # 直接提取文本，避免对 Tag 对象做正则替换
    content = content[2].get_text(" ", strip=True)
    print(content)

