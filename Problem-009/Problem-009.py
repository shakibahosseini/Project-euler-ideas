"""
Problem No.9 from Project Euler
Author: Shakiba Hosseini
Created on : 29.06.2025
"""

flag = False

for a in range(1, 1000):
    for b in range(1, 1000):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print(f'a: {a}')
            print(f'b: {b}')
            print(f'c: {c}')
            print(f'abc: {a*b*c}')
            flag = True
            break
        
    if flag == True:
        break