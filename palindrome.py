import sys

if len(sys.argv) < 2:
    print("Please provide a string to check.")
    print("Usage: python palindrome.py <string>")
    sys.exit(1)

string = sys.argv[1]

if string == string[::-1]:
    print(f"{string} is a Palindrome")
else:
    print(f"{string} is not a Palindrome")