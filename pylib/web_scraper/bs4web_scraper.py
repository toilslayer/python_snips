import requests
from bs4 import BeautifulSoup

def bs4_scrape(url,start,end):
    response = requests.get(url)
    soup1 = BeautifulSoup(response.text, 'html.parser')
    pretty_page = soup1.prettify()
    line_page = soup1.get_text().split('\n')

    web_portion=[]
    found=0
    for line in line_page:
        if start in line:
            found = 1
        if found == 1:
            web_portion.append(line)
        if end in line:
            break
    print(web_portion)
