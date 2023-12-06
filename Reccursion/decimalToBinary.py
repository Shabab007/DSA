def decToBinary(n):
  assert int(n)== n, "the number must be integer"
  if (n==0):
    return 0
  else:    
    return n % 2 + 10 * decToBinary(int(n/2))