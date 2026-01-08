import math

num = int(input("Enter a number: "))

if num >= 1:
    sqrt_of_num = math.sqrt(num)
    print(f"square root of {num} is {sqrt_of_num}")
else:
    print("Error: Square root is only defined for numbers greater than or equal to 1.")

if num <= 0:
    print("Error: Natural logarithm is only defined for numbers greater than 0.")
else:
    natural_log = math.log(num)
    print(f"Logarithm :{natural_log}")

sine_of_num = math.sin(num)
print(f"Sine of {num} is {sine_of_num}")