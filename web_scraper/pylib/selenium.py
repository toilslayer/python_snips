from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def selenium_scrape(url):
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--no-sandbox") 
    chromeOptions.add_argument("--disable-setuid-sandbox") 
    chromeOptions.add_argument("--headless")
    chromeOptions.add_argument("--remote-debugging-port=8003")
    chromeOptions.add_argument("--disable-dev-shm-using") 
    chromeOptions.add_argument("--disable-extensions") 
    chromeOptions.add_argument("--disable-gpu") 
    chromeOptions.add_argument("disable-infobars")
    driver = webdriver.Chrome(options=chromeOptions)
    driver.get(url)
    print(url) 