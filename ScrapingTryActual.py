from bs4 import BeautifulSoup
import requests

#html = requests.get('https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=INR').text
html = requests.get('https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=CAD').text

soup = BeautifulSoup(html, 'lxml')
content = soup.find('p', class_ = 'result__BigRate-sc-1bsijpp-1 iGrAod')
print(content.text)
