import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')

soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.titleline')
subtext = soup.select('.subtext')

def sort_hn(hnlist):
   return sorted(hnlist, key= lambda k : k['count'], reverse=True)
     

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        votes = subtext[idx].select('.score')
        if len(votes):
                points = int(votes[0].getText().replace(' points', ''))
                if points > 99:
                     hn.append({'title': title, 'link': href, 'count': points})
                
    return sort_hn(hn)

pprint.pprint(create_custom_hn(links, subtext))