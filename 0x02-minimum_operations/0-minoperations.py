#!/usr/bin/python3
def minOperations(n):
if n <= 1:
return n

operations = 0
clipboard = 1  # Initial content of clipboard (single 'H')
buffer = 1     # Initial content of buffer (single 'H')

while buffer < n:
    if n % buffer == 0:
        clipboard = buffer  # Update clipboard if buffer divides n
    buffer += clipboard    # Paste the content of clipboard to buffer
    operations += 1        # Increment the number of operations

return operations

Test cases

print("Min # of operations to reach 4 chars:", minOperations(4))
print("Min # of operations to reach 12 chars:", minOperations(12))
