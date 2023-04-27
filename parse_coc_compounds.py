import os
import json
from utils import find_comp_exact
import requests




src = "https://raw.githubusercontent.com/CodeWithSwastik/inorganic-coc/main/compounds.json"

os.system(f"wget -O COC-compounds.txt {src}")
with open("COC-compounds.txt") as f:
  dict = json.load(f)




S = requests.Session()
URL = "https://en.wikipedia.org/w/api.php"
PARAMS = {
    "action": "query",
    "format": "json",
    "list": "search"
}



with open("Not-in-db.txt","a") as f:
  for k,v in dict.items():
    if find_comp_exact(k).startswith("Does not") and find_comp_exact(k.replace("NH4", "[NH4]")).startswith("Does not") and find_comp_exact(k.replace("(", "[").replace(")","]")).startswith("Does not"):
      PARAMS["srsearch"] = k
      R = S.get(url=URL, params=PARAMS)
      DATA = R.json()
      name = DATA['query']['search'][0]['title']
      if name:
        f.write(f"{name} - {k}\n")
      else:
        f.write(f"None - {k}\n")



