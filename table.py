import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://ticker.finology.in/"

r = requests.get(url)
# print(r)
# r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
table = soup.find("table", class_="table table-sm table-hover screenertable")
#print(table)
headers = table.find_all("th")
titles = []
for i in headers:
    title = i.text
    titles.append(title)
df = pd.DataFrame(columns=titles)
rows = table.find_all("tr")
for i in rows[1:]:
    data = i.find_all("td")
    row = [tr.text.strip() for tr in data]
    #print(row)
    l = len(df)
    df.loc[l] = row
print(df)
df.to_csv("stcok_market_data.csv")


#print(df)
#print(titles)




