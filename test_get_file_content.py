from functions.get_file_content import get_file_content

print("get_file_content(\"calculator\", \"lorem.txt\"):")
result = get_file_content("calculator", "lorem.txt")
print(f"Length: {len(result)}")
print(f"Ends with truncation: {result.endswith(']')}")
print(f"Truncated message present: {'truncated at 10000 characters' in result}")

print("\nget_file_content(\"calculator\", \"main.py\"):")
result = get_file_content("calculator", "main.py")
print(result)

print("\nget_file_content(\"calculator\", \"pkg/calculator.py\"):")
result = get_file_content("calculator", "pkg/calculator.py")
print(result)

print("\nget_file_content(\"calculator\", \"/bin/cat\"):")
result = get_file_content("calculator", "/bin/cat")
print(result)

print("\nget_file_content(\"calculator\", \"pkg/does_not_exist.py\"):")
result = get_file_content("calculator", "pkg/does_not_exist.py")
print(result)