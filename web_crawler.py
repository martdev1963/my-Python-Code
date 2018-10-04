import requests
from bs4 import BeautifulSoup
import pandas

r=requests.get("http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")

# store content of requests object...
c=r.content
#print(c)

soup=BeautifulSoup(c,"html.parser")
#print(soup.prettify())

# generate's a list object of all <div> elements...
all=soup.find_all("div",{"class":"propertyRow"})

all[0].find("h4",{"class":"propPrice"}).text.replace("\n","")

page_nr=soup.find_all("a",{"class":"Page"})[-1].text # soup returns a string...
print(page_nr) # page_nr is a string... you must convert to int...

l=[]
base_url="http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
for page in range(0,int(page_nr)*10,10): # start at 0, upto page, and iterate by 10...
    print(base_url+str(page)+"html")
    r=requests.get(base_url+str(page)+".html")
    c=r.content
    soup=BeautifulSoup(c,"html.parser")  # BeautifulSoup returns a list object...
    all=soup.find_all("div",{"class":"propertyRow"})
    for item in all:
            # Dictionary, key/value pairs to store the scraped property info...
            d={}
            item.find()  # grabs first occurence of item being searched
            # span tag below has two elements of data, ergo index 0 and index 1
            d["Address"]=item.find_all("span",{"class","propAddressCollapse"})[0].text # returns a list with specified criterior result...
            try:
                d["Locality"]=item.find_all("span",{"class","propAddressCollapse"})[1].text
            except:
                d["Locality"]=None

            d["Price"]=item.find("h4",{"class","propPrice"}).text.replace("\n","").replace(" ","")
            try:
                d["Beds"]=item.find("span",{"class","infoBed"}).find("b").text
            except:
                d["Beds"]=None

            try:
                d["Area"]=item.find("span",{"class","infoSqFt"}).find("b").text
            except:
                #pass   # this makes python ignore any would be exception...
                d["Area"]=None
            try:
                d["Full Baths"]=item.find("span",{"class","infoValueFullBath"}).find("b").text
            except:
                d["Full Baths"]=None

            try:
                d["Half Baths"]=item.find("span",{"class","infoValueHalfBath"}).find("b").text
            except:
                d["Half Baths"]=None

            for column_group in item.find_all("div",{"class":"columnGroup"}):
                print(column_group)
                for feature_group, feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})):
                    print(feature_group.text, feature_name.text)
                    if "Lot Size" in feature_group.text:
                        d["Lot Size"]=feature_name.text

            # append the dict to the list...
            l.append(d)

import pandas
df=pandas.DataFrame(l)
df
df.to_csv("martyOutput.csv")
