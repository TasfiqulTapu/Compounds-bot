from bs4 import BeautifulSoup
import re

def parse_compounds(html):
    soup = BeautifulSoup(html, 'html.parser')
    compounds = []
    for li in soup.find_all('li'):
        a = li.find('a')
        if a:
          name = a.text
          formula = li.find('span', class_='chemf nowrap').text if li.find('span', class_='chemf nowrap') else ''
          if formula != '':
            compounds.append((name, formula))
    return compounds

def parse_extras(html):
    all = re.findall(r'<li><a href="[A-Za-z0-9\/_= "]*>([A-Za-z ]*)<\/a> \– ([A-Za-z0-9 \(\)]*)<\/li>',html)
    return all

def main():
  with open("List_of_inorganic_compounds",'r') as file:
    txt = file.read()
    extra = parse_extras(txt)
    cmpnds = parse_compounds(txt)
    with open("Compounds_wiki.txt",'a') as f:
      for c in cmpnds:
        f.write(f"{c[0]} - {c[1]}\n")
      for c in extra:
        f.write(f"{c[0]} - {c[1]}\n")
    


if __name__ == "__main__":
  main()