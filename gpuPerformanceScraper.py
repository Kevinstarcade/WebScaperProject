from bs4 import BeautifulSoup
import re
import requests

# define soup
def gpuScraper():
    url = requests.get("https://www.tomshardware.com/reviews/gpu-hierarchy,4388-2.html")
    soup = BeautifulSoup(url.text, "html.parser")

    tableEntries = soup.findAll("td")
    gpuRegex = re.compile(
    r'(?i)\b(?:'  # Case-insensitive, word boundary
    r'(?:rtx|gtx|rx|radeon\s)?\s?'  # Optional prefix (RTX/GTX/RX/Radeon)
    r'\d{3,4}'  # Model number (3-4 digits)
    r'(?:\s?(?:ti|super|xt|x|pro)){0,2}'  # Optional suffixes (0-2 terms)
    r')\b',
    re.IGNORECASE
    )
    fpsRegex = re.compile(r'\b\d{2,3}\.\d\s?fps\b', re.IGNORECASE)

    gpuDict = {}
    
    for i in range(0, len(tableEntries), 6):
        if (re.search(gpuRegex, tableEntries[i].text)):
            gpu = tableEntries[i].text.lower().split(" ")
            gpu = "".join(gpu[2:])
            if gpu in gpuDict:
                break
            fps = re.search(fpsRegex, tableEntries[i+2].text)
            # print(gpu, fps.group()[:-3])
            gpuDict[gpu] = float(fps.group()[:-3])

    return gpuDict



if __name__ == "__main__":
    ret = gpuScraper()
    for e in ret:
        print(e, ret[e])
    print(len(ret))