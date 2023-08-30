# <p>The cube, $41063625$ ($345^3$), can be permuted to produce two other cubes: $56623104$ ($384^3$) and $66430125$ ($405^3$). In fact, $41063625$ is the smallest cube which has exactly three permutations of its digits which are also cube.</p>
# <p>Find the smallest cube for which exactly five permutations of its digits are cube.</p>

from typing import Dict, List

cubic_dict: Dict[int, List[int]] = {}

for i in range(1000):
    cubic = i**3
    if len(str(cubic)) in cubic_dict:
        cubic_dict[len(str(cubic))].append(cubic)
    else:
        cubic_dict[len(str(cubic))] = [cubic]

    
