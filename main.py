import requests

from beautifulsoup4 import BeautifulSoup

response = requests.get('https://www.bbc.com/news')

print(response.status_code)
# if returns status 200, that means request was successful

# print(response.content) use this to print all content

soup = BeautifulSoup(response.content, 'html.parser')
print(soup)
# save page within element

print(soup.find_all('h2'))
# use this to find any element you want

# Figure out beautifulsoup Import




