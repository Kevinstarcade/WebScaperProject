from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from gpuPerformanceScraper import gpuScraper

# searchPrompt = input()

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/marketplace/edmonton/search/?query=gpu")


closeButton = driver.find_element(By.CSS_SELECTOR, "[aria-label=Close]")
closeButton.click()


soup = BeautifulSoup(driver.page_source, "html.parser")
titles = soup.findAll('span', attrs={'class':'x1lliihq x6ikm8r x10wlt62 x1n2onr6'})
price = soup.findAll('span', attrs={'class':'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x676frb x1lkfr7t x1lbecb7 x1s688f xzsf02u'})
gpusDict = gpuScraper()


gpus = {'1650','1660','1050','1060','1070','1080',
        '2060','2070','2080',
        '3050','3060','3070','3080','3090',
        '4060','4070','4080','4090',
        '5700','6600','6650','6700','6750','6800','6900','6850',
        '7600','7700','7800','7900'}

for i in range(len(titles)):
    listing = titles[i].text.lower()
    # print(listing)

    for gpu in gpus:
        if gpu in listing:
            if f"{gpu} ti" in listing or f"{gpu}ti" in listing:
                gpu += " ti"
            if f"{gpu} super" in listing or f"{gpu}super" in listing:
                gpu += " super"
            if f"{gpu} xtx" in listing or f"{gpu}xtx" in listing:
                gpu += " xtx"
            elif f"{gpu} xt" in listing or f"{gpu}xt" in listing:
                gpu += " xt"
            print(gpu, price[i].text, gpusDict(gpu))
