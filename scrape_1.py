import requests
from bs4 import BeautifulSoup
import pandas
from collections import OrderedDict

id_list = []

request = requests.get("https://www.fifa.com/worldcup/players/_libraries/byposition/[id]/_players-list")
soup = BeautifulSoup(request.content,"html.parser")

for ids in range(0,736):
	all = soup.find_all("a","fi-p--link")[ids]
	id_list.append(all['data-player-id'])

df = pandas.DataFrame({
"Ids":id_list
})

base_url = "https://www.fifa.com/worldcup/players/player/"
player_list = []

for pages in id_list:
	d=OrderedDict()
	print(base_url+str(pages)+"/profile.html")
	request = requests.get(base_url+str(pages)+"/profile.html")
	content = request.content
	soup = BeautifulSoup(content,"html.parser")
	try:
		d['Name'] = soup.find("div",{"class":"fi-p__name"}).text.replace("\n","").strip()
		print(d['Name'])
		d['Country'] = soup.find("div",{"class":"fi-p__country"}).text.replace("\n","").strip()
		d['Role'] = soup.find("div",{"class":"fi-p__role"}).text.replace("\n","").strip()
		d['Age'] = soup.find("div",{"class":"fi-p__profile-number__number"}).text.replace("\n","").strip()
		d['Height(cm)'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[1].text.replace("\n","").strip()
		d['International Caps'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[2].text.replace("\n","").strip()
		d['International Goals'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[3].text.replace("\n","").strip()
		player_list.append(d)
	except:
		print("unable to parse profile")
	
df = pandas.DataFrame(player_list)
df.to_csv('players_info.csv', index = False)
print(df.head())

