from urllib import request
from bs4 import BeautifulSoup
url = 'http://www.17k.com/chapter/2933095/36699279.html'
headers = {'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
page = request.Request(url, headers=headers)
page_info = request.urlopen(page).read().decode('utf-8')
soup = BeautifulSoup(page_info, 'html.parser')
titles = soup.find_all('a', 'title')
try:
    file = open('E:\titles.txt', 'w')
        for title in titles:
            file.write(title.string,'\n')
finally:
    if file:
        file.close()