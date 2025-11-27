import sys

if len(sys.argv) < 2:
    print("Usage: python even_odd_count.py <num1> <num2> ...")
    sys.exit(1)

script_name = sys.argv[0]

try:
    numbers = list(map(int, sys.argv[1:]))
except:
    numbers = []   # force else block to trigger

even_count = 0
odd_count = 0

if len(numbers) > 0:
    for n in numbers:
        if n % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
else:
    # Default list (same style as grade program defaults)
    numbers = [1, 2, 3, 4, 5]

    even_count = 2   # 2, 4
    odd_count = 3    # 1, 3, 5

print("script Name:", script_name)
print("Even Count:", even_count)
print("Odd Count:", odd_count)
