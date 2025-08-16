"""
Problem No.12 from Project Euler
Author: Shakiba Hosseini
Created on : 26.07.2025
"""

# Triangle numbers: T = n*(n+1) // 2
from tqdm import tqdm


def M(v):
    count = 0
    for i in range(1, int(v**0.5)+1):
        if v%i == 0:
            count += 2 if i != v//i else 1
            # beacause when i ** 2 = v, then we have two duplicate value
    return count
    

def T(n):
    return n*(n+1) // 2

for i in tqdm(range(1, 1000000000000)):
    tri = T(i)
    
    if M(tri) > 500:
        print()
        print('The first triangle number with over five hundred divisors:',tri)
        break