import sys
from functions.write_file import write_file

# Test 1: Write to an existing file
print("Test 1: Write to existing file (lorem.txt)")
result1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print(result1)
print()

# Test 2: Write to a new file in a subdirectory
print("Test 2: Write to new file in subdirectory (pkg/morelorem.txt)")
result2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print(result2)
print()

# Test 3: Attempt to write outside the working directory
print("Test 3: Attempt to write outside working directory (/tmp/temp.txt)")
result3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print(result3)
