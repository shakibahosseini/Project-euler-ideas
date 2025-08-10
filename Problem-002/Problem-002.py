"""
Problem no.2 from Project Euler
Author: Shakiba Hosseini
Created on : 28.06.2025
"""

a, b = 1, 2     # first two Fibonacci terms
total = 0

if a % 2 == 0:
    total += a
if b % 2 == 0:
    total += b
    
c = a + b

while c < 4000000:
    if c % 2 == 0:
        total += c
    a, b = b, c
    c = a + b
        
print("Sum:", total)