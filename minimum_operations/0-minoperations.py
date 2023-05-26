#!/usr/bin/python3
import math

def minOperations(n):
    if n == 1:
        return 0  # Already have 1 H character, no operations needed
    if n < 1:
        return 0  # Invalid input, impossible to achieve
    
    operations = [float('inf')] * (n + 1)  # Initialize the operations list with infinity
    operations[1] = 0  # Base case
    
    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                # If j is a divisor of i, it means we can copy j characters and paste i//j times to get i characters
                operations[i] = min(operations[i], operations[j] + i // j)
    
    return operations[n]  # Return the minimum number of operations for n

# Example usage:
#n = 9
#result = minOperations(n)
#print("Number of operations:", result)

