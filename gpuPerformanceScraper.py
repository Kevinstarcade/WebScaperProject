from bs4 import BeautifulSoup
import re
import requests

# define soup
def gpuScraper():
    url = requests.get("https://www.tomshardware.com/reviews/gpu-hierarchy,4388.html")
    soup = BeautifulSoup(url.text, "html.parser")

    tableEntries = soup.findAll("td")
    lastGpu = soup.find("td", string=re.compile("GT 1030"))
    endList = tableEntries.index(lastGpu)

    gpuNames = tableEntries[0:endList+1:7]
    gpuFPS = tableEntries[2:endList+8:7]

    dict = {}
    gpus = {'1650','1660','1050','1060','1070','1080',
            '2060','2070','2080',
            '3050','3060','3070','3080','3090',
            '4060','4070','4080','4090',
            '5700','6600','6650','6700','6750','6800','6900','6850',
            '7600','7700','7800','7900'
            }

    for i in range(len(gpuNames)):
        for gpu in gpus:
            if gpu in gpuNames[i].text.lower():
                if f"{gpu} ti" in gpuNames[i].text.lower():
                    gpu += " ti"
                if f"{gpu} super" in gpuNames[i].text.lower():
                    gpu += " super"
                if f"{gpu} xtx" in gpuNames[i].text.lower():
                    gpu += " xtx"
                elif f"{gpu} xt" in gpuNames[i].text.lower():
                    gpu += " xt"

                if "fps" in gpuFPS[i].text:
                    dict.update({gpu:float(gpuFPS[i].text[gpuFPS[i].text.index('(')+1:gpuFPS[i].text.index('f')])})

    return dict