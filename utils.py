import itertools
import re

def elem_dict_to_str(dic):
  str = ' '
  for k,v in dic.items():
    str += (k + " ")
  return str

def ultra_inefficient_find(elems):
  di = {} 
  combs = get_combinations(elems) 
  for a in combs:
    data = inefficient_find(parse_elems("".join(a)))
    di.update(data)
  return di



def inefficient_find(elems):
  
  all = {}
  with open("Compounds.txt", "r") as f:
    for line in f:
      ret = does_it_contain(elems, line)
      if ret:
        all[ret[0]]= ret[1]

  return all
        

def does_it_contain(elems, line): 
  if len(line) < 2: 
    return False
  name, _formula = line.split(" - ")
  formula = _formula.replace("[","").replace("]","")
  for k,v in elems.items():
    if (k + " ") not in elem_dict_to_str(parse_elems(formula.strip())):
      return False
  
  f_elems = parse_elems(formula.strip())
  str_of_elems = elem_dict_to_str(elems)
  #print(str_of_elems, f_elems)
  for k,v in f_elems.items():
    if (k + ' ')  not in str_of_elems:
      #print(str_of_elems)
      #print(f_elems)
      #print(elems)
      return False
  return (name, _formula)

def get_combinations(dct):
    keys = list(dct.keys())
    combinations_list = []
    for i in range(1, len(keys) + 1):
        combinations_list += list(itertools.combinations(keys, i))
    return combinations_list


def parse_elems(compound):
    # Create an empty dictionary to store elements and their corresponding count
    elem_dict = {}
    compound = compound.strip()
    # Split the compound string by the non-alphabetic characters to extract each element and its count
    split_compound = re.findall('[A-Z][a-z]*\d*', compound)
    
    # Iterate through each element in the split compound list
    for elem in split_compound:
        # Use regular expression to separate the element symbol and its count (if any)
        elem_name, elem_count = re.match('([A-Z][a-z]*)(\d*)', elem).groups()
        
        # If no count was specified, assume it's 1
        if elem_count == '':
            elem_count = 1
        else:
            elem_count = int(elem_count)
        
        # Add the element and its count to the dictionary
        if elem_name in elem_dict:
            elem_dict[elem_name] += elem_count
        else:
            elem_dict[elem_name] = elem_count
    
    # getting the missed ones
    elem_dict_w_missed = count_in_bracs(compound,elem_dict)
    return elem_dict_w_missed

def count_in_bracs(compound,dict):
    if "(" not in compound: return dict
    if ")" not in compound: return dict
    bracs = re.findall('\(([A-Za-z0-9]*)\)(\d*)',compound)
    missed = dict
    for g in bracs:
        l = parse_elems(g[0])
        n = int(g[1] or 1)
        for k,v in l.items():
          missed[k] += v * (n -1)
            
    return missed

def add_comp_txt(name,formula):
    with open("Compounds.txt", "r") as f:
      for line in f:
        if formula + "\n" in line:
          return f"Formula already exists\n{line}"
        elif not find_comp_all(name).startswith("Does not exist"):
         return f"That name already exists"
      
    with open("Compounds.txt","a") as f:
      f.write(f"{name} - {formula}\n")
    return f"Compound added\n{name} - {formula}"


def find_comp_exact(formula):
    with open("Compounds.txt", "r") as f:
      for line in f:
        if f" {formula}\n" in line:
          return line
    return "Does not exist in DB"

def find_comp_all(formula):
    data = ""
    with open("Compounds.txt", "r") as f:
      for line in f:
        if f"{formula}" in line:
          data += line
    return data or "Does not exist in DB"

