from bs4 import BeautifulSoup
import requests
url ="https://docs.google.com/spreadsheets/d/1gmr8siZdUniQ6n7dvtfthlnHaWmpJX7VqRivvN4hmz8/edit?ts=5e79c3f4#gid=0"
req=requests.get(url)
soup=BeautifulSoup(req.text,"html.parser")
print(soup)