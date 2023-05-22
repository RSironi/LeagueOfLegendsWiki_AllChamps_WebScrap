#Utiliza a técnica de WebScrap para obter dados referente League of Legends

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

url = "https://leagueoflegends.fandom.com/wiki/List_of_champions"


option = Options()
option.headless= True
driver = webdriver.Edge(options=option)

driver.get(url)

element = driver.find_element(By.XPATH,"//*[@id='mw-content-text']/div[1]/table[2]")
htmlContent = element.get_attribute("outerHTML")

soup = BeautifulSoup(htmlContent,'html.parser')
leagueTable = soup.find('table')

listChampions=[]
listChampionsImg=[]
fields=['champion','champimgsrc']

for champions in leagueTable.find_all('tbody'):
    champion = champions.find_all('tr')
    for row in champion:
        championName = row.find('span')['data-champion'] # o [coloca a tag] e sucesso!
        championImg = row.find('img')['data-src']
        listChampions.append(championName)
        listChampionsImg.append(championImg)


dict = {'championsName':listChampions,'championsUrlImg':listChampionsImg}

df=pd.DataFrame(dict)
df.to_csv('AllChampionsList.csv')

driver.quit()
