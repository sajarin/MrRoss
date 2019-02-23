from urllib.request import urlopen as uReq 
from bs4 import BeautifulSoup as soup
from scrap import deeper

root_url = "https://www.chamber.nyc/"
my_url = root_url + "directory.asp"

#opening up a connection and parsing the page 
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#parse html
page_soup = soup(page_html, "html.parser")

#grab each section 
containers = page_soup.findAll("li")

#for each subdirectory, scrap the contact info of each business
for container in containers: 
    new_url = root_url + container.a["href"]
    deeper(new_url, 0)

    

