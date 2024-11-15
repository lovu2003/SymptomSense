import re
from googlesearch import search
import warnings

warnings.filterwarnings("ignore")
import requests
from bs4 import BeautifulSoup

# Take input a disease and return the content of wikipedia's infobox for that specific disease


def diseaseDetail(term):
    diseases = [term]
    ret = term + "\n"
    for dis in diseases:
        query = dis + " wikipedia"
        for sr in search(query, tld="co.in", stop=10, pause=0.5):
            match = re.search(r"wikipedia", sr)
            
            if match:
                wiki = requests.get(sr, verify=False)
                soup = BeautifulSoup(wiki.content, "html5lib")
                # Fetch HTML code for 'infobox'
                info_table = soup.find("table", {"class": "infobox"})
                if info_table:
                    details = {}
                    rows = info_table.find_all("tr")
                    for row in rows:
                        columns = row.find_all(["th", "td"])
                        if len(columns) >= 2:
                            key = columns[0].text.strip()
                            value = columns[1].text.strip()
                            details[key] = value
                    return details
                
    return ret
