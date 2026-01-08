def facto_recursive(n):
    if n == 0:
        return 1
    return n * facto_recursive(n-1)

num = input("Enter a number: ")
if num.isdigit():
    if int(num) >= 0:
        result = facto_recursive(int(num))
        print(f"Factorial of {num} is {result}")
else:
    print("Error: Invalid input. or type a non-negative integer.")