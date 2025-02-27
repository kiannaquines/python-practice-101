names = ["kian","james","irish","jearard","arden","francis"]

def reverse(str):
    return str[::-1]
    
mapped_names = map(reverse, names)

for name in mapped_names:
    print(name)
    
from typing import List

def reverse_names(names:List[str]):
    revered_names_temp = []
    for name in names:
        revered_names_temp.append(name[::-1])
        
    return revered_names_temp
    

print(reverse_names(names=names))
