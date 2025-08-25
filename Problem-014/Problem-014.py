"""
Problem No.14 from Project Euler
Author: Shakiba Hosseini
Created on : 10.08.2025
"""

from tqdm import tqdm

def func(n):
    if n % 2 == 0:
        m = n // 2
    elif n % 2 != 0:
        m = (3*n) + 1
        
    return m



flag = False
longest_chain = 1
I = 0

for i in tqdm(range(1, 1000000)):
    start_number = i
    count = 1
    
    while i != 1:
        count += 1
        i = func(i)
    
    if count > longest_chain:
        longest_chain = count
        I = start_number
        flag = True
        
print()   
if flag:
    print(f'The number {I} has the longest chain with length {longest_chain}.')
    