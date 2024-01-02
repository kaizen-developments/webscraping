#Print desired links from an <article URL> of the form '/wiki/<Article_Name>'!
#Take in a Wikipedia article URL
#of the form /wiki/<Article_Name> and return a list of all linked
#particle URLs in the same form with a function named 'getLinks'!
#Call getLinks with a starting article, choose
#a random article link from the returned list, and call getLinks
#again, until you stop the program or until no article links are found
#on the new page with the main function!


from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

import sys

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))

def main():
    links = getLinks(sys.argv[1])
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs['href']
        print(newArticle)
        links = getLinks(newArticle)

main()

#TODO: Define the Six Degrees of Wikipedia problem!