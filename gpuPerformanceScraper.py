from bs4 import BeautifulSoup
import re
import requests

# open the driver in chrome
# options = webdriver.ChromeOptions()
# options.add_argument("--ignore-certificate-errors")
# options.add_argument("--ignore-certificate-errors-spki-list")
# options.add_argument("--ignore-ssl-errors")
# options.add_argument("--allow-insecure-localhost")
# options.add_argument("--disable-web-security")
# driver = webdriver.Chrome(options=options)
# driver.get("https://www.tomshardware.com/reviews/gpu-hierarchy,4388.html")

# define soup
url = requests.get("https://www.tomshardware.com/reviews/gpu-hierarchy,4388.html")
soup = BeautifulSoup(url.text, "html.parser")

tableEntries = soup.findAll("td")
lastGpu = soup.find("td", string=re.compile("GT 1030"))
endList = tableEntries.index(lastGpu)

gpuNames = tableEntries[0:endList+1:7]
gpuFPS = tableEntries[2:endList+8:7]

for i in range(len(gpuFPS)):
    if "fps" in gpuFPS[i].text:
        print(gpuNames[i].text + ',', gpuFPS[i].text[gpuFPS[i].text.index('(')+1:gpuFPS[i].text.index('f')])
    else:
        print(gpuNames[i].text + ',', None)
