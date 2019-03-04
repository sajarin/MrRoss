from urllib.request import urlopen as uReq 
from bs4 import BeautifulSoup as soup

def deeper(url, num):
    #opening up a connection and parsing the page 
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()

    #parse page html
    page_soup = soup(page_html, "html.parser")
    #grab each listing from the page 
    listings = page_soup.findAll("div",{"class": "businessListing"})

    filename = "leads.csv"
    f = open(filename, "a+")

    #for each subdirectory, scrap the contact info of each business
    for listing in listings: 
        span = listing.findAll("span", {"class": "valValue"})
        floating_div = listing.find("div", {"class": "floatRightDiv"})
        quick_info = floating_div.findAll("a", {"class": "medium"})

        if len(span) == 3 and len(quick_info) == 3: #only scrap listings that have all information
            try:
                business_name = listing.b.a.text
                business_address = span[0].text
                business_number = span[1].text
                business_contact = span[2].text
                business_email = quick_info[2]["href"]
                business_website = quick_info[1]["href"]
                print(business_website)
                f.write(business_name.replace(",", " ") + "," + business_address.replace(",", " ") + "," + business_contact.replace(",", " ") + 
                             "," + business_number + "," + business_email + "," + business_website + "\n")
            except AttributeError:
                pass

    tr = page_soup.table.table.findAll("tr")
    td = tr[2].tr.findAll("td") 
    
    #if this page has a navigation bar, then it has multiple pages
    if(len(td) > 1): 

        table = page_soup.findAll("table")
        arrow_img  = table[2].tr.span.findAll("img") #check the second tr and grab the next arrow img tag
        check_next = arrow_img[1]["src"] #grab the img tag source 

        if(check_next == "images/zevie_fwdbut.gif"): #if the img is the next page button, run deeper on the next page 
            if(num == 0): 
                #the first page starts at both 1 and 0, so add two to get to the second page
                page_num = num + 2 
                num_string = str(page_num) 
                new_url = url + "&page=" + num_string 
            else:
                #if it's not the first page, just add by one 
                page_num = num + 1 
                num_string = str(page_num) 
                new_url = url[:-1] + num_string
            #call deeper recursively until there are no deeper pages
            deeper(new_url, page_num)

url = "https://www.chamber.nyc/directory_cat.asp?catid=216"
num = 0
deeper(url, num)


