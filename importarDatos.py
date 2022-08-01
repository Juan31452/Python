import requests
from bs4 import BeautifulSoup as b

#url = "https://dimayor.com.co/estadisticas/"
url = "https://www.ebay.com/globaldeals"

html = requests.get(url)
content = html.content
soup = b(content,"lxml")
#print(soup)

contenido =  soup.find("h3",{"class":"dne-itemtile-title ellipse-3"})
print(contenido)