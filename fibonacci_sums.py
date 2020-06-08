def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif 1 < n <= 30:
        return fibonacci(n-1) + fibonacci(n-2)

n = eval(input("Enter a number: "))
print(fibonacci(n))