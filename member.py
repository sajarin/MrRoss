from urllib.request import urlopen as uReq 
from bs4 import BeautifulSoup as soup

#This function scraps the Member Business Directory provided by the nYC DIrectory of COmmerce
def page(url, num): 
   
    n = str(num)
    url = url + n
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()

    #parse page html
    page_soup = soup(page_html, "html.parser")
    #grab each listing from the page 
    listings = page_soup.findAll("div",{"class": "business"})

    filename = "member.csv"
    f = open(filename, "a+")

    for listing in listings: 
        business_info = listing.div.findAll("span") 
        
        business_name = listing.h3.text
        business_contact = business_info[0].text[14:]
        business_number = business_info[1].text[7:]
        business_email = business_info[2].text[7:]
        business_website = business_info[3].text[9:]
        business_address = business_info[4].text[9:]
        
        print(business_website)

        f.write(business_name.replace(",", " ") + "," + business_address.replace(",", " ") + "," + business_contact.replace(",", " ") + "," + business_number + "," + business_email + "," + business_website + "\n")
        
