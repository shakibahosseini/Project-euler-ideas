"""
Problem No.10 from Project Euler
Author: Shakiba Hosseini
Created on: 19.07.2025
"""

from tqdm import tqdm

total = 0
for i in tqdm(range(2, 2000001)):
    is_prime = True
    
    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            is_prime = False
            break
        
    if is_prime:
        total += i
        
print("\n")
print(f"total is equal to: {total}")