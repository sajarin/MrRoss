import requests

def scrape_and_save_page(storage_path, url):
    response = requests.get(url)
    html = response.text
    with open(f'{storage_path}', 'w') as f:
        f.write(html)