from urllib.request import urlopen as uReq 
from bs4 import BeautifulSoup as soup

#This function scraps the Member Business Directory provided by the NYC DIrectory of COmmerce
#page takes is given the base url and the page number represented by the variable num 
#This program works sequentially, scraping page by page, with main.py incrementing the page number
def page(url, num): 
  
    #convert num into a string and append it to the url 
    page_num = str(num)
    url = url + page_num 

    #establish a connection to the url using urlopen
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()

    #parse page html
    page_soup = soup(page_html, "html.parser")
    #grab each listing from the page 
    listings = page_soup.findAll("div",{"class": "business"})

    #create a file to store scraped values 
    filename = "member.csv"
    f = open(filename, "a+", encoding="utf-8")


    #for each business on the page grab their name, number, email, website, address and business owner
    for listing in listings: 
        business_info = listing.div.findAll("span") 
        business_name = listing.h3.text
        business_contact = business_info[0].text[14:]
        business_number = business_info[1].text[7:]
        business_email = business_info[2].text[7:]
        business_website = business_info[3].text[9:]
        business_address = business_info[4].text[9:]
        
        print(business_website)

        #append these values to the csv file member.csv
        f.write(business_name.replace(",", " ") + "," + 
                business_address.replace(",", " ") + "," + 
                business_contact.replace(",", " ") + "," + 
                business_number + "," + 
                business_email + "," + 
                business_website + "\n")
        
