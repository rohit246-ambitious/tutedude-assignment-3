def facto_recursive(n):
    if n == 0:
        return 1
    return n * facto_recursive(n-1)

num = int(input("Enter a number: "))
if num >= 0:
    result = facto_recursive(num)
    print(f"Factorial of {num} is {result}")
else:
    print("Error: Factorial is not defined for negative numbers.")