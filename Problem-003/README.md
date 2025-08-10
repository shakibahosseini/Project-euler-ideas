Problem 003 – Largest prime factor

Problem Statement:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

---
Math Note:

To check if a number *i* is prime, we only test divisors from 2 up to the square root of *i*. Because if *i* has a factor bigger than its square root, it also has a smaller one. So checking more is not needed and makes the code faster.
