from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

page=urllib.request.urlopen("https://www.flipkart.com/search?q=iphone%2013&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
soup=BeautifulSoup(page,"html.parser")

pname=[]
pprice=[]
prating=[]
pfeatures=[]

for i in soup.findAll("div",class_="_3pLy-c row"):
    getpname=i.find("div",attrs={"class":"_4rR01T"})
    getpprice=i.find("div",attrs={"class":"_30jeq3 _1_WHN1"})
    getprating=i.find("div",attrs={"class":"_3LWZlK"})
    getpfeatures=i.find("ul",attrs={"class":"_1xgFaf"})
    pname.append(getpname.text)
    pprice.append(getpprice.text)
    prating.append(getprating.text)
    pfeatures.append(getpfeatures.text)

data=pd.DataFrame({'product_name':pname,'price':pprice,'Product_ratings':prating,'Features':pfeatures})
print(data)

data.to_csv("Flipkart.csv")