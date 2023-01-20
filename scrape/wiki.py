'''Web scraping functions'''

import re
import requests
from bs4 import BeautifulSoup
from utils.functions import formatted_name


class Person:
    '''Blueprint of searched person'''
    URL: str = 'https://pl.wikipedia.org/wiki/'


    def __init__(self, name: str, surname: str) -> None:
        '''Initialize person's name'''
        session = requests.Session()
        session.get(self.URL)
        response = session.get(
            url=self.URL + formatted_name(name, surname), 
            headers=session.headers, 
            cookies=session.cookies
        )
        self.soup = BeautifulSoup(response.content, 'html.parser')


    def get_name(self) -> str:
        '''Scraping person's full name'''
        return self.soup.find('span', {'class', 'mw-page-title-main'}).text.strip()


    def get_date_of_birth(self) -> str:
        '''Scraping person's date of birth'''
        tr_tags = self.soup.select('tr')
        title_attrib_pattern = re.compile(r'.*?title="(\d[^"]+)')

        for tag in tr_tags:
            if 'miejsce urodzenia' in str(tag):
                result = ''
                for match in title_attrib_pattern.finditer(str(tag)):
                    result += match.group(1) + ' '
                if result == '':
                    result = re.search('.*?>(\d[^<]+)', str(tag)).group(1)
                return result.strip()

    def get_image(self) -> str:
        '''Scraping person's image'''
        tr_tag_with_image = self.soup.find('tr', {'class': 'grafika iboxs'})
        return re.search('.*?src="([^"]+)', str(tr_tag_with_image)).group(1)
