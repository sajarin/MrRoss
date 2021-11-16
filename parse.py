from bs4 import BeautifulSoup

def load_html(file_path: str) -> BeautifulSoup:
    try: 
        with open(file_path, 'r') as f:
            raw_html = f.read()
            soup = BeautifulSoup(raw_html, 'lxml')
            return soup
    except OSError as err:
        print("OSError: {0}".format(err))

def parse_html(page_soup: BeautifulSoup) -> str:
    listings = page_soup.findAll("div", {"class": "business"}) 
    for listing in listings: 
        business_info = listing.div.findAll("span") 
        business_name = listing.h3.text
        business_contact = business_info[0].text[14:]
        business_number = business_info[1].text[7:]
        business_email = business_info[2].text[7:]
        business_website = business_info[3].text[9:]
        business_address = business_info[4].text[9:]
        
        return (business_name.replace(",", " ") + "," + 
                business_address.replace(",", " ") + "," + 
                business_contact.replace(",", " ") + "," + 
                business_number + "," + 
                business_email + "," + 
                business_website + "\n")