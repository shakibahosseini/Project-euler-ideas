"""
Problem No.16 from Project Euler
Author: Shakiba Hosseini
Created on : 29.06.2025
"""

n = 2 ** 1000
Sum_digits = 0
while n > 0:
    Sum_digits += n % 10
    n = n // 10
    
print(Sum_digits)
