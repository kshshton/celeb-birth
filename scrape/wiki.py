'''Web scraping functions'''

from bs4 import BeautifulSoup
from utils.functions import formatted_name
import re
import requests

URL = 'https://pl.wikipedia.org/wiki/'


def date_of_birth(name: str, surname: str) -> str:
    '''Scraping date of birth for named person'''
    session = requests.Session()
    session.get(URL)
    response = session.get(url=URL + formatted_name(name, surname), headers=session.headers, cookies=session.cookies)
    soup = BeautifulSoup(response.content, 'html.parser')

    tr_tags = soup.select('tr')
    title_attrib_pattern = re.compile(r'.*?title="(\d[^"]+)')

    for tag in tr_tags:
        if 'miejsce urodzenia' in str(tag):
            result = ''
            for match in title_attrib_pattern.finditer(str(tag)):
                result += match.group(1) + ' '
            if result == '':
                result = re.search('.*?>(\d[^<]+)', str(tag)).group(1)
            return result
