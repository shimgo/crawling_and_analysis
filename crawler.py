import requests
from bs4 import BeautifulSoup
from parser import Parser
from race_id import RaceId
from race_result import RaceResult
from urllib.parse import urljoin
import time
import datetime
import sys

class Crawler:
    def __init__(self, parser = "html.parser"):
        self.__parser = parser

    def get(self, url):
        res = requests.get(url)   
        return BeautifulSoup(res.content, self.__parser)

SAPPORO   = 1
HAKODATE  = 2
FUKUSHIMA = 3
NIGATA    = 4
TOKYO     = 5
NAKAYAMA  = 6
TYUKYO    = 7
KYOTO     = 8
HANSHIN   = 9
OGURA     = 10

crawler     = Crawler()
YEAR        = {'start': 2017, 'end': 2017}
DAYS        = {'start': 1,    'end': 3}
PERFORMANCE = {'start': 1,    'end': 1}
RACE        = {'start': 1,    'end': 99}
areas       = [SAPPORO, HAKODATE, FUKUSHIMA, NIGATA,
               TOKYO, NAKAYAMA, TYUKYO, KYOTO, HANSHIN, OGURA]

url_base = sys.argv[1]

for year in range(YEAR['start'], YEAR['start'] + 1):
    for area in areas:
        for performance in range(PERFORMANCE['start'], PERFORMANCE['end'] + 1):
            for day in range(DAYS['start'], DAYS['end'] + 1):
                for race in range(RACE['start'], RACE['end'] + 1):
                    url = urljoin(url_base,
                                  str(year) +
                                  str(area).zfill(2) +
                                  str(performance).zfill(2) +
                                  str(day).zfill(2) + 
                                  str(race).zfill(2))
                    print("Get: " + url)
                    html = crawler.get(url)

                    race_id = RaceId()
                    race_results = Parser.parse_race(html, race_id.increment())

                    print(race_results)
                    if race_results:
                        RaceResult.save_all(race_results)
                    else:
                        break

                    time.sleep(1)
