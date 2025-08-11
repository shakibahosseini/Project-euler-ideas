Problem 007 – 10001st prime

Problem Statement:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?

---
Notes:

- *tqdm* : A Python library showing a progress bar for loops, useful to track progress during long operations.
  
- *Divisor check limit up to the square root* : if a number has a factor larger than its square root, the corresponding pair factor is smaller. So checking up to the square root is enough to confirm primality efficiently.
