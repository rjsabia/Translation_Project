import os
import openai
import requests
import bs4 # Beautiful Soup 4

# Environmental variables
openai.api_key = os.getenv('OPEN_AI_KEY_01')

# -------------------------

country = input("What country are you interested in for news?")
# print(country)

# Countries for this project
# SPAIN, FRANCE  <-- for now (Latin based)
# Newspaper urls
#  - lemonde.fr/en/ and elpais.com

country_newspaper = {"Spain":"https://elpais.com/",
                    "France": 'https://www.lemonde.fr/'}

# Test Dictionary --- below ----
# print(country_newspaper[country])

url = country_newspaper[country]
result = requests.get(url)
# print(result.text)

# Lemonde tag class
tag = 'article__title-label'

soup = bs4.BeautifulSoup(result.text,'lxml')
# soup.select('.article__title-label')

# soup.select('.article__title')[:3]

print(soup.select('.article__title')[:3])


















