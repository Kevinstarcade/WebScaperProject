import re
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from gpuPerformanceScraper import gpuScraper
import numpy as np
import matplotlib.pyplot as plt

# searchPrompt = input()

def normalizeString(string : str) -> str:
    """
    makes the string lowercase, removes spaces and prefixes (rtx, gtx, rx)

    Args:
        string (str): the string to normalize

    Returns:
        str: normalized string
    """
    if not string: 
        return None
    
    prefix = re.compile(r'(?i)(?:rtx|gtx|rx|radeon)')  # Optional prefix (RTX/GTX/RX/Radeon) )
    string = re.sub(prefix, "", string)
    return string.lower().replace(" ", "")

def plotArrays(x, y, title="", xlabel="", ylabel=""):
    plt.plot(x, y, 'o')
    plt.xlabel("Price")
    if title:
        plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    plt.show()

def main():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/marketplace/edmonton/search/?query=gpu")

    closeButton = driver.find_element(By.CSS_SELECTOR, "[aria-label=Close]")
    closeButton.click()
    sleep(1)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    allTitles = soup.findAll('span', attrs={'class':'x1lliihq x6ikm8r x10wlt62 x1n2onr6'})
    allPrices = soup.findAll('span', attrs={'class':'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x676frb x1lkfr7t x1lbecb7 x1s688f xzsf02u'})
    allLinks = soup.findAll('a', attrs={'class':'x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xkrqix3 x1sur9pj x1s688f x1lku1pv'})

    # driver.close()

    gpusDict = gpuScraper()

    gpuRegex = re.compile(
        r'(?i)\b(?:'  # Case-insensitive, word boundary
        r'(?:rtx|gtx|rx|radeon)?\s?'  # Optional prefix (RTX/GTX/RX/Radeon)
        r'\d{3,4}'  # Model number (3-4 digits)
        r'(?:\s?(?:ti|super|xt|x|pro|\d*\s?gb)){0,3}'  # Optional suffixes (0-2 terms)
        r')\b',
        re.IGNORECASE
    )

    validGpus = []
    validPrices = []
    validFps = []
    validLinks = []

    for i in range(len(allTitles)):
        gpu = re.search(gpuRegex, allTitles[i].text)
        price = allPrices[i].text[3:]
        if "," in price:
            price = price.replace(",", "")
        link = "https://facebook.com" + allLinks[i]['href']
        if gpu:
            NormalizedGpu = normalizeString(gpu.group())
            if NormalizedGpu in gpusDict:
                validGpus.append(gpu.group())
                validPrices.append(int(price))
                validFps.append(gpusDict[NormalizedGpu])
                validLinks.append(link)

    print(f"{"GPU" : <15} {"| Price": <8} {" | FPS": <10} | Link")
    print("-"*100)
    for i in range(len(validGpus)):
        print(f"{validGpus[i]: <15} | {validPrices[i]: <7} | {validFps[i]: <7} | {validLinks[i]}")

    plotArrays(np.array(validPrices), np.array(validFps), xlabel="Price", ylabel="FPS")

if __name__ == "__main__":
    main()