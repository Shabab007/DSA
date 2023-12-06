def sumofDigts(n):
    assert n >= 0 and int(n)==n, "number has to be a positive integer."
    if n == 0:
        return 0
    else:
        return int(n %10) + sumofDigts(int(n/10))

print(sumofDigts(-111))