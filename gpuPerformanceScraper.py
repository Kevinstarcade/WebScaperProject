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
print(url.text)
soup = BeautifulSoup(url.text, "html.parser")
gpus = soup.findAll('a', attrs={'data-label':'x'})
# entries = soup.findAll('td', attrs={'class':'table_body__data'})








# works
# entries = soup.findAll('td', string=re.compile("fps"))

# for entry in entries:
#     print(entry.text)

    