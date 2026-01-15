import sys
from functions.run_python_file import run_python_file

# Test 1: Run calculator main with no args (should print usage)
print("Test 1: Run calculator main.py (no args)")
result1 = run_python_file("calculator", "main.py")
print(result1)
print()

# Test 2: Run calculator with args
print("Test 2: Run calculator main.py with args ['3 + 5']")
result2 = run_python_file("calculator", "main.py", ["3 + 5"])
print(result2)
print()

# Test 3: Run calculator tests
print("Test 3: Run calculator tests.py")
result3 = run_python_file("calculator", "tests.py")
print(result3)
print()

# Test 4: Attempt to run file outside working directory
print("Test 4: Attempt to run ../main.py (outside directory)")
result4 = run_python_file("calculator", "../main.py")
print(result4)
print()

# Test 5: Attempt to run non-existent file
print("Test 5: Attempt to run nonexistent.py")
result5 = run_python_file("calculator", "nonexistent.py")
print(result5)
print()

# Test 6: Attempt to run non-Python file
print("Test 6: Attempt to run lorem.txt (not a .py file)")
result6 = run_python_file("calculator", "lorem.txt")
print(result6)
