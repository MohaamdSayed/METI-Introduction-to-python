def fibonacci(n: int) -> int:
  if n == 0:
      return 0
  elif n == 1:
      return 1
  else:
      return fibonacci(n - 1) + fibonacci(n - 2)

# Test the function
n = 5  # Example: Find the 10th Fibonacci number
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")