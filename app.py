import requests
from bs4 import BeautifulSoup


URL = 'https://ostrovok.ru/hotel/russia/moscow/?q=2395&dates=12.04.2023-13.04.2023&guests=1&cur=RUB&price=one&utm_source=hotelsru.affiliate.bb1&utm_medium=partners&partner_slug=hotelsru.affiliate.bb1e&sid=45d4a3e1-d2f5-4bbc-96df-cf1346ab08e0'
# URL = 'https://101hotels.com/main/cities/moskva'
# URL = 'https://ostrovok.ru/hotel/russia/?q=153'
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

hotels = soup.find_all('h2', class_='zen-hotelcard-name')
prices = soup.find_all('div', class_='zen-hotelcard-rate-price')

names: list[str] = []
pricess: list[str] = []

for hotel in hotels[:10]:
    names.append(hotel.text.strip())
for price in prices[:10]:
    pricess.append(price.text.strip())
    
for i in range(len(names)):
    print(f'name - {names[i]} \nprice - {pricess[i]}')