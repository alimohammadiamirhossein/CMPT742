# Function to check if a number is prime (basic solution)
def is_prime_basic(n):
    # TODO: Implement a basic check for prime numbers
    if n <= 1:
        return False
    return ...

# Optimized prime number check function
def is_prime_optimized(n):
    # TODO: Implement an optimized prime check for large numbers
    if n <= 1:
        return False
    return ...


# Define main function
def main():
    num = 29
    print(is_prime_basic(num))  # Expected output: True
    print(is_prime_optimized(num))  # Expected output: True


if __name__ == "__main__":
    main()