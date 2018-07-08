import urllib
import urllib.request
from bs4 import BeautifulSoup
import os  # must import os library otherwise you get error: NameError: name 'os' is not defined for line 30

  # function definition to fetch the URL and parse the data
def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

playerdatasaved = ""
soup = make_soup("https://www.basketball-reference.com/players/a/")
for record in soup.findAll('tr'):
    playerdata=""
    for data in record.findAll('td'):
      # print(record.text)
      # print(data.text)
      playerdata=playerdata + "," + data.text # data from the td tag
    if len(playerdata)!=0:
  # print(playerdata)
        playerdatasaved = playerdatasaved + "\n" + playerdata[1:]

header = "Player,From,To,Pos,Ht,Wt,Birth Date,College"
file = open(os.path.expanduser("Basketball_1.csv"), "wb")
file.write(bytes(header, encoding="ascii",errors='ignore'))
file.write(bytes(playerdatasaved, encoding="ascii",errors='ignore'))

#print(playerdatasaved)

"""
---------------------------------------------------------------------------------------------------------------------
Introduction to Web Scraping(Python) - Lesson 02 (Scrape Tables) saves to csv file. SAF Business Analytics

---------------------------------------------------------------------------------------------------------------------
"""
