"""
Problem No.1 from Project Euler
Author: Shakiba Hosseini
Created on : 28.06.2025
"""


total = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        total += i
        
print("Sum:", total)