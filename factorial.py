# Write a Python function that takes an integer as input and calculates its factorial
def factorial (n):
        fact = 1
        for i in range(1, n + 1):
            fact = fact*i
        return fact
n = int(input("Enter positive number 'N': "))
f = factorial(n)
print('factorial is: ', f)
