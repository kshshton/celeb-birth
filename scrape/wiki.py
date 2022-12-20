from bs4 import BeautifulSoup
from lxml import etree
from utils.functions import formatted_name
import requests

URL = 'https://pl.wikipedia.org/wiki/'
HEADERS = {'date': 'Tue, 20 Dec 2022 14:28:20 GMT', 'vary': 'Accept-Encoding,Cookie,Authorization', 'server': 'ATS/9.1.3', 'x-content-type-options': 'nosniff', 'content-language': 'pl', 'last-modified': 'Mon, 19 Dec 2022 13:52:43 GMT', 'content-type': 'text/html; charset=UTF-8', 'content-encoding': 'gzip', 'age': '32322', 'x-cache': 'cp3058 hit, cp3050 hit/16', 'x-cache-status': 'hit-front', 'server-timing': 'cache;desc="hit-front", host;desc="cp3050"', 'strict-transport-security': 'max-age=106384710; includeSubDomains; preload', 'report-to': '{ "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }', 'nel': '{ "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}', 'set-cookie': 'WMF-Last-Access=20-Dec-2022;Path=/;HttpOnly;secure;Expires=Sat, 21 Jan 2023 12:00:00 GMT, WMF-Last-Access-Global=20-Dec-2022;Path=/;Domain=.wikipedia.org;HttpOnly;secure;Expires=Sat, 21 Jan 2023 12:00:00 GMT, Path=/; secure; Domain=.wikipedia.org', 'accept-ch': 'Sec-CH-UA-Arch,Sec-CH-UA-Bitness,Sec-CH-UA-Full-Version-List,Sec-CH-UA-Model,Sec-CH-UA-Platform-Version', 'permissions-policy': 'interest-cohort=(),ch-ua-arch=(self "intake-analytics.wikimedia.org"),ch-ua-bitness=(self "intake-analytics.wikimedia.org"),ch-ua-full-version-list=(self "intake-analytics.wikimedia.org"),ch-ua-model=(self "intake-analytics.wikimedia.org"),ch-ua-platform-version=(self "intake-analytics.wikimedia.org")',  'cache-control': 'private, s-maxage=0, max-age=0, must-revalidate', 'accept-ranges': 'bytes', 'content-length': '23715'}


def date_of_birth(name: str, surname: str) -> str:
    '''Fetching date of birth for named person'''
    response = requests.get(URL + formatted_name(name, surname), HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    dom = etree.HTML(str(soup))
    return dom.xpath('//*[@id="mw-content-text"]/div[1]/table/tbody/tr[3]/td/p/span')[0].text
