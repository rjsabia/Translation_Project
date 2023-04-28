import os
import openai
import requests
import bs4 # Beautiful Soup 4

# Environmental variables
openai.api_key = os.getenv('OPEN_AI_KEY_01')

# -------------------------

# country = input("What country are you interested in for news?")
# print(country)

# Countries for this project
# SPAIN, FRANCE  <-- for now (Latin based)
# Newspaper urls
#  - lemonde.fr/en/ and elpais.com

# country_newspaper = {"Spain":"https://elpais.com/",
                   # "France": 'https://www.lemonde.fr/'}

# COUNTRY: (URL,TAG)
# country_newspaper = {"Spain":("https://elpais.com/",'.c_t'),
                    # "France":('https://www.lemonde.fr/','.article__title-label')}

# Test Dictionary --- below ----
# print(country_newspaper[country])

# url = country_newspaper[country]
# result = requests.get(url)
# print(result.text)

# Lemonde tag class
# tag = 'article__title-label'

# soup = bs4.BeautifulSoup(result.text,'lxml')

# ----Testing functionality below -----
# soup.select('.article__title-label')
# soup.select('.article__title')[:3]
# print(soup.select('.article__title')[:3])

# for item in soup.select('.article__title')[:3]:
    # print(item.getText())

# COUNTRY: (URL,TAG)
country_newspaper = {"Spain":("https://elpais.com/",'.c_t'),
                    "France":('https://www.lemonde.fr/','.article__title-label')}

                    # "France":('https://www.lemonde.fr/','.article__title-label')}

def create_prompt():
    country = input("What country would you like a news summary from?")
    
    # Catch for non listed countries
    try:
        url,tag = country_newspaper[country]
    except:
        print("Sorry, country not supported at this time : ( )")
        return

    # Start web scraping if supported
    results = requests.get(url)
    soup = bs4.BeautifulSoup(results.text,'lxml')

    country_headlines = ''
    for item in soup.select(tag)[:3]:
        country_headlines += item.getText()+'\n'

    prompt = "Detect the language of the news headlines below, then translate a summary of the headlines to English in a conversational tone.\n"

    return prompt + country_headlines

# print(create_prompt())
prompt = create_prompt()
print(prompt)

response = openai.Completion.create(
            model='text-davinci-003',
            prompt=prompt,
            max_tokens=250,
            temperature=0.1,
            top_p=1.0
)

print(response['choices'][0]['text'])













    
     

    


    

     












 



















