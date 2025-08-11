"""
Problem No.7 from Project Euler
Author: Shakiba Hosseini
Created on : 29.06.2025
"""

from tqdm import tqdm

C = True
L = []
for i in tqdm(range(2, 1000000)):
    C = True
    
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            C = False
            break
        
    if C == True:
        L.append(i)        
    

print()
P = L[10000]
print(f'The 10001th Prime number is: {P}')