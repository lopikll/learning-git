def calculate_factorial(number):
    # Initialize the factorial result to 1
    factorial = 1

    # Loop from 1 to number (inclusive) and multiply factorial by each number
    for i in range(1, number + 1):
        factorial *= i

    return factorial

print(calculate_factorial(5))
print(calculate_factorial(7))
print(calculate_factorial(9))
print(calculate_factorial(10))
