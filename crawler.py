import requests
from bs4 import BeautifulSoup
from parser import Parser
from race_id import RaceId
from race_result import RaceResult

class Crawler:
    def __init__(self, parser = "html.parser"):
        self.__parser = parser

    def get(self, url):
        res = requests.get(url)   
        return BeautifulSoup(res.content, self.__parser)

crawler = Crawler()
html = crawler.get("http://db.netkeiba.com/race/201905021010/")

race_id = RaceId()
race_results = Parser.parse_race(html, race_id.increment())

print(race_results)

if race_results:
    RaceResult.save_all(race_results)
