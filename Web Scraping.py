from bs4 import BeautifulSoup, NavigableString
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

html = requests.get("https://www.aoml.noaa.gov/hrd/hurdat/International_Hurricanes.html")

soup = BeautifulSoup(html.content, 'lxml')

filename = "International_Atlantic_Hurricanes_Landfalls.csv"
f = open(filename, "w")

tablerows = 0
souptable = soup.find("td", {"id": "tdcontent"})
for record in souptable.findAll("tr"):
    if(isinstance(record, NavigableString)):
        continue
    tbltxt = ""
    tablerows = tablerows + 1
    print(f"We are on tablerow {tablerows}" )
    tdlist = record.findAll('td')
    print(tdlist)
    if(len(tdlist) != 10):
        continue
    for data in tdlist:
        tbltxt = tbltxt + data.text.strip() + "|"
        tbltxt = tbltxt.replace('%', '')
    tbltxt = tbltxt[0:-1] + '\n'
    f.write(tbltxt)
f.close()

hurricanedf = pd.read_csv("International_Atlantic_Hurricanes_Landfalls.csv", delimiter= "|")
hurricanedf['Date'] = pd.to_datetime(hurricanedf['Date'])
monthcount = hurricanedf['Date'].groupby([hurricanedf['Date'].dt.month]).agg({'count'})
print(monthcount)

hurricanedf['latlon'] = hurricanedf['Latitude'] + ' ' + hurricanedf['Longitude']
print(hurricanedf['latlon'].value_counts())

yearcount = hurricanedf['Date'].groupby([hurricanedf['Date'].dt.year]).agg({'count'})
yearplot = sns.lineplot(yearcount)
plt.ylabel("Count")
plt.title("Landfall Count Over Time")
plt.show()
plt.clf()

maxwindcount = hurricanedf["Max  Winds (kt)"].groupby([hurricanedf['Date'].dt.year]).agg({'mean'})
maxwindplot = sns.lineplot(maxwindcount)
plt.ylabel("Max Winds (kt)")
plt.title("Max Winds (kt) Over Time")
plt.show()
plt.clf()
annualcatcount = hurricanedf["SS  HWS"].groupby([hurricanedf['Date'].dt.year]).agg({'mean'})
annualcatplot = sns.lineplot(annualcatcount)
plt.ylabel("Count")
plt.title("Annual Category Count Over Time")
plt.show()
