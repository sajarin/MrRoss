from urllib.request import urlopen as uReq 
from bs4 import BeautifulSoup as soup
from certified import deeper
from member import page

while True:
    try:
        user_in = int(input("Type 0 for scraping Member Directory or 1 for scraping Certified Business Directory \n"))
    except ValueError: 
        print("Sorry invalid input")
        continue
    else:
        break

root_url = "https://www.chamber.nyc/"
if (user_in == 0):
    my_url = root_url + "directory.php?search=&page="

    filename = "member.csv"
    f = open(filename, "a+", encoding="utf-8")
    headers = "Business, Address, Contact, Number, Email, Website\n"
    f.write(headers)
    for x in range(1,68):
        page(my_url, x)
if (user_in == 1):

    my_url = root_url + "directory.asp"

    #opening up a connection and parsing the page 
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    #parse html
    page_soup = soup(page_html, "html.parser")

    #create a file  called leads.csv and append the headers to the first row 
    filename = "certified.csv"
    f = open(filename, "a+")
    headers = "Business, Address, Contact, Number, Email, Website\n"
    f.write(headers)

    #grab each directory 
    directory = page_soup.findAll("li")

    #for each subdirectory, scrap the contact info of each business
    for subdirectory in directory: 
        new_url = root_url + subdirectory.a["href"]
        deeper(new_url, 0)