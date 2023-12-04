import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.iplt20.com/auction/2021"
r = requests.get(url)
# print(r)

soup = BeautifulSoup(r.text, "lxml")
soup1 = soup.encode("utf-8")
print(soup1)
table = soup1.find('table', {'class': 'ih-td-tab auction-tbl'})
#header = table.find_all("th")

# print(table)