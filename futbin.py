# coding=utf-8
import json
import requests
import bs4 as bs
from requests_html import HTMLSession

class Player():
    
    def __init__(self,name,console,version):
         self.player = getPlayer(name)
         if self.player != None:
             self.id = {ids['version'] : ids['id'] for ids in self.player}
             self.price = price_scrape(console,self.id,version)
             self.name = self.player[0]['full_name']
             self.version = [ver['version'] for ver in self.player]
         
         


def getPlayer(name):
    try:
        response = requests.get('http://www.futbin.com/search?year=19&term=%s' %(name))  
        if 'error' in response.json():
            raise ValueError;
        else:
            schedule = response.json()
            return schedule
    except:
        player = None
        return player

#def getPlayerId(name):
 #   try:
  #      url = ('http://www.futbin.com/search?year=19&term=%s' %(name))
   #     response = requests.get(url)
    #    page = response.text
     #   soup = bs.BeautifulSoup(url, 'html.parser')
      #  playerId = soup.find(id='pge-info')['data-baseid']
       # jsonURL ='https://www.futbin.com/19/playerPrices?player=' + playerId
        #jsonObj = jsonURL.json()
        #psLowestPrice = jsonObj[playerId]['prices']['ps']['LCPrice']
        #return psLowestPrice
   # except:
        
        
        
def price_scrape(console,ids,version):
    url = ('https://www.futbin.com/19/player/%s' %(ids[version]))
    session = HTMLSession()
    r = session.get(url)
    soup = bs.BeautifulSoup(r.content, "lxml")
    tagPrice = soup.find("div", id="page-info")
    player_id = tagPrice["data-player-resource"]
    prices = json.loads(session.get(url[:26]+"playerPrices?player=" + player_id).text)
    livePrice = float(prices[player_id]["prices"][console]["LCPrice"].replace(",", ""))
    r.close()
    return livePrice