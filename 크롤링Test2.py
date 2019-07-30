import json
import requests
from bs4 import BeautifulSoup as bs

for page in range(0,10):
    
    data = requests.get('https://www.coinbit.co.kr/webbbsmain/noticelists/chno-100/&page={}'.format(page)).json()
    
    for i in range(0,10):
        print(data[i]['subject'])

