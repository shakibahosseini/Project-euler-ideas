"""
Problem no.5 from Project Euler
Author: Shakiba Hosseini
Created on : 28.06.2025
"""

from tqdm import tqdm

flag = True
for i in tqdm(range(1, 10000000000)):
    flag = True
    for j in range(1, 21):
        if i % j != 0:
            flag = False
            break
    if flag == True:
        print()
        print(i)
        break