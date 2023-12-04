import requests
from bs4 import BeautifulSoup

url = "https://www.webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

res = requests.get(url)
print(res)
# soup = BeautifulSoup(res.text, "lxml")
# boxes = soup.find_all("div",class_="col-md-4 col-xl-4 col-lg-4")
# for box in boxes:

# #print(len(boxes))
# #for box in range(1,22):
# #box = soup.find_all("div", class_ = "col-md-4 col-xl-4 col-lg-4")
#  name = box.find("a").text
#  desc = box.find("p", class_= "description card-text").text
#  price = box.find("h4", class_="float-end price card-title pull-right").text
#  rate = box.find('div[class_=ratings] p')
#  print(rate)
#  #rating = box.find("p", class_="float-end review-count").text
#  #data = box.find("data-rating")

#  #print(data)
 
