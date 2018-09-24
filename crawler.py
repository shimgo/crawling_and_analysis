import requests
from bs4 import BeautifulSoup
from parser import Parser

class Crawler:
    def __init__(self, parser = "html.parser"):
        self.__parser = parser

    def get(self, url):
        res = requests.get(url)   
        return BeautifulSoup(res.content, self.__parser)

crawler = Crawler()
html = crawler.get("http://db.netkeiba.com/race/201805021010/")

race_results = Parser.parse_race(html)
print(race_results)

