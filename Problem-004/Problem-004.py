"""
Problem no.4 from Project Euler
Author: Shakiba Hosseini
Created on : 19.07.2025
"""

from tqdm import tqdm

factor1 = 0
factor2 = 0
max_palindrome = 0

for i in tqdm(range(100, 1000)):
    
    for j in range(i, 1000):
        product = i*j
        m = str(product)
        m_rev = m[::-1]
        
        if m == m_rev:
            if max_palindrome < product:
                max_palindrome = product
                factor1 = i
                factor2 = j
        
print()
print(f"The largest Palindrome is: {max_palindrome}")
print(f"It is the product of {factor1} × {factor2}")
