from urllib.request import urlopen as uReq 
from bs4 import BeautifulSoup as soup

def deeper(url, int):
    #opening up a connection and parsing the page 
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()

    #parse html
    page_soup = soup(page_html, "html.parser")

    #grab each section 
    listings = page_soup.findAll("div",{"class": "businessListing"})

    #for each subdirectory, scrap the contact info of each business
    for listing in listings: 
        detail = listing.findAll("span", {"class": "valValue"})
        more_details = listing.find("div", {"class": "floatRightDiv"})
        even_more_details = more_details.findAll("a", {"class": "medium"})

        if len(detail) == 3 and len(even_more_details) == 3:
            business_name = listing.b.a.text
            business_address = detail[0].text
            business_number = detail[1].text
            business_contact = detail[2].text

            business_email = even_more_details[1]["href"]
            business_website = even_more_details[2]["href"]
            print(business_email) 
    
    tr = page_soup.table.table.findAll("tr")
    td = tr[2].tr.findAll("td")

    if(len(td) > 1):

        con = page_soup.findAll("table")
        c = con[2].tr.span.findAll("img")
        check_next = c[1]["src"]

        if(check_next == "images/zevie_fwdbut.gif"):
            if(int == 0):
                page_num = int + 2 
            else:
                page_num = int + 1
            num_string = str(page_num) 
            new_url = url + "&page=" + num_string 
            deeper(new_url, page_num)
