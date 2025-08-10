"""
Problem no.3 from Project Euler
Author: Shakiba Hosseini
Created on : 28.06.2025
"""

n = 600851475143
max_prime = 1

for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        flag = True
        
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                flag = False
                break
            
        if flag:
            max_prime = i
            
print(f"The largest prime factor: {max_prime}")
