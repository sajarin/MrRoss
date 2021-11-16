import os
import glob
import scrape
import parse

def save_pages(BASE_URL : str, NUM_OF_PAGES :int) -> None:
    for i in range(1, NUM_OF_PAGES):
        url_to_scrape = BASE_URL + str(i)
        storage_path = f'data/2021/saved_pages/page{i}.html'
        scrape.save_page(storage_path, url_to_scrape)

def run_bot(): 
    BASE_URL = 'https://www.chamber.nyc/directory.php?search=&page='
    NUM_OF_PAGES = 42
    # save_pages(BASE_URL, NUM_OF_PAGES)

    filename = "data/2021/member.csv"
    f = open(filename, "a+", encoding="utf-8")
    for file in sorted(glob.glob('data/2021/saved_pages/*.html'), key=lambda x: int(x.split('\page')[1][:-5])):
        page_soup = parse.load_html(file)
        extracted_data = parse.parse_html(page_soup)
        f.write(extracted_data)

if __name__ == "__main__":
    run_bot()