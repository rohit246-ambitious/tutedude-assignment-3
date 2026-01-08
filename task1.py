def facto_recursive(n):
    if n == 0:
        return 1
    return n * facto_recursive(n-1)

num = int(input("Enter a number: "))
result = facto_recursive(num)
print(f"Factorial of {num} is {result}")