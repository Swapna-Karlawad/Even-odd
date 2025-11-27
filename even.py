import sys

# Check number of arguments
if len(sys.argv) != 6:
    print("Usage: python evenodd.py <n1> <n2> <n3> <n4> <n5>")
    sys.exit(1)

# Script name
script_name = sys.argv[0]

# Read numbers
n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
n3 = int(sys.argv[3])
n4 = int(sys.argv[4])
n5 = int(sys.argv[5])

# List of numbers
numbers = [n1, n2, n3, n4, n5]

even_count = 0
odd_count = 0

# Count even and odd numbers
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Display output
print("Script Name:", script_name)
print("Numbers Entered:", numbers)
print("Count of Even Numbers:", even_count)
print("Count of Odd Numbers:", odd_count)
