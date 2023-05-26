#!/usr/bin/python3
import math

def minOperations(n):
    if n == 1:
        return 0  # Already have 1 H character, no operations needed
    if n < 1:
        return 0  # Invalid input, impossible to achieve
    
    operations = 0

    for i in range(2, int(math.sqrt(abs(n))) + 1):
        while n % i == 0:
            operations += i
            n //= i

    if n > 1:
        
        operations += n
    
    return operations

# Example usage:
#n = 9
#result = minOperations(n)
#print("Number of operations:", result)

