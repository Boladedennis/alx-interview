def minOperations(n):
    if n == 1:
        return 0  # No operations needed for n = 1
    operations = 0
    num_h = 1
    clipboard = 0
    while num_h < n:
        if n % num_h == 0:
            clipboard = num_h  # Copy all
        num_h += clipboard  # Paste
        operations += 1
    if num_h == n:
        return operations
    else:
        return 0  # Impossible to achieve n H characters

# Example usage:
n = 9
result = minOperations(n)
print(f"The fewest number of operations needed to achieve {n} H characters is: {result}")

