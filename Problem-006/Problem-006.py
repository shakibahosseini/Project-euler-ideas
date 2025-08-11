"""
Problem no.6 from Project Euler
Author: Shakiba Hosseini
Created on : 29.06.2025
"""

Sum1 = 0
for i in range(1, 101):
    Sum1 += i

print("The square of the sum:", Sum1**2)

Sum2 = 0
for i in range(1, 101):
    Sum2 += i**2

print("The sum of the squares:", Sum2)
print("Difference:", Sum1**2 - Sum2)
