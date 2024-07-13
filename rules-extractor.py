from bs4 import BeautifulSoup
import requests

base_url = 'https://wikihoghoogh.net'
url = 'https://wikihoghoogh.net/wiki/%D8%B1%D8%AF%D9%87:%D9%85%D9%88%D8%A7%D8%AF_%D9%82%D8%A7%D9%86%D9%88%D9%86_%D9%85%D8%A7%D9%84%DB%8C%D8%A7%D8%AA_%D8%A8%D8%B1_%D8%A7%D8%B1%D8%B2%D8%B4_%D8%A7%D9%81%D8%B2%D9%88%D8%AF%D9%87'

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')
div = soup.find('div', class_='mw-category-group')
links = div.find_all('a')
link_urls = [link['href'] for link in links]

for link in link_urls:
    url = base_url +  link
    print(url)
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')
    div = soup.find('div', class_='mw-parser-output')
    p_tags = div.find_all('p')
    content = ''
    for p_tag in p_tags:
        content += p_tag.get_text()
        # content += '\n'
    print(content)
    
    with open("rules.txt", "a", encoding="utf-8") as file:
        file.write(content)
        file.write('\n\n----------------------------------------------------\n\n')
