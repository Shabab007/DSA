def factorial(n):
    if n < 0 or int(n)!=n:
       return False
    if n in [0,1]:
        return 1
    else:
        return n*factorial(n-1)


print(factorial(1.1))
print(factorial(5))
print(factorial(-1))